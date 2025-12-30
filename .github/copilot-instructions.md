# Copilot instructions for RaspberryJuice

Be concise and practical: this repository is a small Bukkit/Spigot plugin that implements
the Minecraft Pi socket API. Focus on the networking/server-threading model, command
handlers in RemoteSession, and the build/deploy steps used by Java plugin developers.

- **Big picture**: The plugin starts `ServerListenerThread` (TCP listener) from
  `RaspberryJuicePlugin.onEnable()` which accepts sockets and constructs a `RemoteSession`.
  `RemoteSession` spawns input/output threads and enqueues messages; the plugin's scheduler
  calls `RemoteSession.tick()` to handle queued commands on the main server thread.
  Key files: `src/main/java/net/zhuoweizhang/raspberryjuice/RaspberryJuicePlugin.java`,
  `src/main/java/net/zhuoweizhang/raspberryjuice/ServerListenerThread.java`,
  `src/main/java/net/zhuoweizhang/raspberryjuice/RemoteSession.java`.

- **Concurrency & safety notes**:
  - `ServerListenerThread` accepts connections and calls `plugin.handleConnection()`.
  - `RaspberryJuicePlugin.sessions` is mutated inside `handleConnection()` (synchronized).
  - `RemoteSession` uses per-connection `inQueue`/`outQueue` plus dedicated threads; heavy
    work is pulled into `tick()` so avoid long blocking operations in that method.
  - `maxCommandsPerTick` exists to limit work; prefer incremental processing.

- **Command handling pattern**: `RemoteSession.handleCommand()` parses Pi-API-style method
  names (e.g., `world.getBlock`, `player.setPos`) and dispatches with many if/else branches.
  When modifying or adding commands follow the existing parse-and-send pattern and use
  the helper methods already in `RemoteSession` for locations and block updates.

- **Configuration & runtime**:
  - Default config: `src/main/resources/config.yml` — `hostname`, `port`, `location` (RELATIVE|ABSOLUTE),
    and `hitclick` (LEFT|RIGHT|BOTH).
  - Plugin entry: `src/main/resources/plugin.yml` sets `main` to
    `net.zhuoweizhang.raspberryjuice.RaspberryJuicePlugin`.

- **Build & test**:
  - Build with Maven: `mvn package`. The produced jar is in `target/`.
  - Tests use Cucumber + TestNG (see `pom.xml` test deps). Running `mvn test` may require
    a test classpath that provides Bukkit; tests are present under `test/` and resources.
  - `pom.xml` excludes `src/main/resources/mcpi` and `test` from normal resources; treat
    `src/main/resources/mcpi` as example client libs only.

- **Deploy / debug**:
  - Run inside a Spigot/Bukkit server: copy `target/raspberryjuice-*.jar` into the server's `plugins/`
    folder and start the server.
  - For local debugging, attach your IDE remote debugger to a running server JVM.

- **Project-specific conventions**:
  - Many API semantics mirror Minecraft PI; prefer compatibility with clients using
    strings like `world.getBlock` and CSV-style responses.
  - Locations are often sent/returned as relative to `origin` — see `LocationType` usage
    in `RaspberryJuicePlugin` and `RemoteSession`.
  - Avoid changing the wire protocol format without updating `RemoteSession.handleCommand()`.

- **Files to look at for changes or examples**:
  - README: `README.md` (project overview and build instructions)
  - Plugin start: `src/main/java/net/zhuoweizhang/raspberryjuice/RaspberryJuicePlugin.java`
  - Network acceptor: `src/main/java/net/zhuoweizhang/raspberryjuice/ServerListenerThread.java`
  - Command dispatch and helpers: `src/main/java/net/zhuoweizhang/raspberryjuice/RemoteSession.java`
  - Config and plugin metadata: `src/main/resources/config.yml`, `src/main/resources/plugin.yml`

If any of the above sections are unclear or you want examples distilled into quick tasks
(e.g., "add a new command world.foo"), tell me which part to expand and I will update this file.
