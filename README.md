> **_NOTE:_** RaspberryJuice is end of life, no further releases are planned. [Read about why](https://github.com/zhuowei/RaspberryJuice/pull/84#issuecomment-544295161). The repository will remain open for issues but no PRs will be accepted. Thank you for the fun times.

# RaspberryJuice

A Bukkit plugin which implements the Minecraft Pi Socket API.

## Commands

### Commands supported

 - world.get/setBlock
 - world.getBlockWithData
 - world.setBlocks
 - world.getPlayerIds
 - world.getBlocks
 - chat.post
 - events.clear
 - events.block.hits
 - player.getTile
 - player.setTile
 - player.getPos
 - player.setPos
 - world.getHeight
 - entity.getTile
 - entity.setTile
 - entity.getPos
 - entity.setPos

### Commands that can't be supported

 - Camera angles

### Extra commands

 - getBlocks(x1,y1,z1,x2,y2,z2) has been implemented
 - getDirection, getRotation, getPitch functions - get the 'direction' players and entities are facing
 - setDirection, setRotation, setPitch functions - set the 'direction' players and entities are facing
 - getPlayerId(playerName) - get the entity of a player by name
 - pollChatPosts() - get events back for posts to the chat
 - setSign(x,y,z,block type id,data,line1,line2,line3,line4)
   - Wall signs (id=68 or block.SIGN_WALL.id) require data for facing direction 2=north, 3=south, 4=west, 5=east
   - Standing signs (id=63 or block.SIGN_STANDING.id) require data for facing rotation (0-15) 0=south, 4=west, 8=north, 12=east
 - spawnEntity(x,y,z,entity) - creates an entity and returns its entity id. see entity.py for list.
 - getEntityTypes - returns all the entities supported by the server.
 - entity.getName(id) - get a player name for entity id. Reverse of getPlayerId(playerName)
 - getEntities - get all currently loaded entities list by optional entity type id
 - removeEntity - removes entity with specified id
 - removeEntities - removes all currently loaded entities by optional entity type id
 - entity.getEntities - get currently loaded entities list near specified entity by optional entity type id
 - entity.removeEntities - removes currently loaded entities near specified entity, by optional entity type id
 - player.getEntities - get currently loaded entities list near specified player entity id by optional entity type id
 - player.removeEntities - removes currently loaded entities near specified player entity id, by optional entity type id
 - events.pollProjectileHits - get events back of arrow hit
 - player.pollProjectileHits - get events back of arrow hit for the player
 - player.pollBlockHits - get block hits for the player
 - player.pollChatPosts - get events back for posts to the chat for the player
 - player.clearEvents - clear events for the player
 - entity.pollProjectileHits - get events back of arrow hit for an entity
 - entity.pollBlockHits - get block hits for an entity
 - entity.pollChatPosts - get events back for posts to the chat for an entity
 - entity.clearEvents - clear events for this entity
 - entity.addPassenger(vehicleId, passengerId) - mounts passengerId onto vehicleId
 - entity.setEquipment(entityId, slot, material, *enchantments) - sets equipment for a living entity
 - entity.addPotionEffect(entityId, effectName, duration=600, amplifier=0) - adds a potion effect to an entity
 - player.addPotionEffect(effectName, duration=600, amplifier=0) - adds a potion effect to the player
 - player.getTileLookingAt(distance=200) - gets the tile coordinates the player is looking at
 - player.strikeLightning(x, y, z) - strikes lightning at offset from player's position
 - player.strikeLightningAtSelf() - strikes lightning at player's current position
 - world.strikeLightning(x, y, z) - strikes lightning at absolute coordinates
 - world.strikeLightningEffect(x, y, z) - visual-only lightning strike at coordinates
 - world.strikeLightningAtEntity(entityId) - strikes lightning at an entity's location
 - world.setWeather(weatherType, duration=None) - sets weather ('clear', 'sun', 'rain', 'storm', 'thunder', 'lightning')
 
Note - extra features are NOT guaranteed to be maintained in future releases, particularly if updates are made to the original Pi API which replace the functionality

## Config

Modify config.yml:

 - hostname: - ip address or hostname to allow connections from, default is "0.0.0.0" (any). "localhost" would prevent remote clients from connecting.
 - port: 4711 - the default tcp port can be changed in config.yml
 - location: RELATIVE - determine whether locations are RELATIVE to the spawn point (default like pi) or ABSOLUTE
 - hitclick: RIGHT - determine whether hit events are triggered by LEFT clicks, RIGHT clicks or BOTH 

## Libraries

To use the extra features an modded version of the java and python libraries that were originally supplied by Mojang with the Pi is required, [github.com/zhuowei/RaspberryJuice/tree/master/src/main/resources/mcpi](https://github.com/zhuowei/RaspberryJuice/tree/master/src/main/resources/mcpi).  

You only need the modded libraries to use the extra features, the original libraries supplied with Minecraft Pi edition still work, you just wont be able to use the extra features

## Build

To build RaspberryJuice, [download and install Maven](https://maven.apache.org/install.html), clone the repository, run `mvn package':

```
git clone https://github.com/zhuowei/RaspberryJuice
cd RaspberryJuice
mvn package
```

## Version history

 - 26.2 - Updated Spigot dependency to 26.2, fixed block ID mapping and spear aliases
 - 26.1.2 - Updated Java to 26 and Spigot to 26.1.2, added BlockIdMapper for backward compatibility, expanded Python API with new capabilities (lightning, weather, equipment, potions, passengers)
 - 1.12.2 - Added compiled jar for raspberryjuice-1.12.2
 - 1.12.1 - hostname specified in config.yml
 - 1.12 - getEntities, removeEntities, pollProjectileHits, events calls by player and entity
 - 1.11 - spawnEntity, setDirection, setRotation, setPitch
 - 1.10.1 - bug fixes
 - 1.10 - left, right, both hit clicks added to config.yml & fixed minor hit events bug
 - 1.9.1 - minor change to improve connection reset
 - 1.9 - relative and absolute positions added to config.yml
 - 1.8 - minecraft version 1.9.2 compatibility
 - 1.7 - added pollChatPosts() & block update performance improvements
 - 1.6 - added getPlayerId(playerName), getDirection, getRotation, getPitch
 - 1.5 - entity functions
 - 1.4.2 - bug fixes
 - 1.4 - bug fixes, port specified in config.yml
 - 1.3 - getHeight, multiplayer, getBlocks
 - 1.2 - added world.getBlockWithData
 - 1.1.1 - block hit events
 - 1.1 - Initial release

## Contributors

 - [zhuowei](https://github.com/zhuowei)
 - [martinohanlon](https://github.com/martinohanlon)
 - [jclaggett](https://github.com/jclaggett)
 - [opticyclic](https://github.com/opticyclic)
 - [timcu](https://www.triptera.com.au/wordpress/)
 - [pxai](https://github.com/pxai)
 - [RonTang](https://github.com/RonTang)
 - [Marcinosoft](https://github.com/Marcinosoft)
 - [neuhaus](https://github.com/neuhaus)
