#Martin O'Hanlon
#www.stuffaboutcode.com
#RaspberryJuice Tests

import original.mcpi.minecraft as minecraft
import modded.mcpi.minecraft as minecraftmodded
import original.mcpi.block as block
import modded.mcpi.block as blockmodded
import modded.mcpi.entity as entitymodded
import time
import math
import datetime
import random
from McUtility import check_is_night_in_game, spawn_mobs_behind_player_at_night, print_connected_players, spawn_skeleton_rider, spawn_zombie_rider, make_player_skeleton_rider

# #Modded Library Tests
mc = minecraftmodded.Minecraft.create("localhost")

# Print all connected players with absolute coordinates
print_connected_players(mc)




# Initial check
is_night = check_is_night_in_game(mc)
if is_night:
    print("It is night in Minecraft.")
else:
    print("It is day in Minecraft.")

username = "Vincent_Craft3r"
target_id = None
player_ids = mc.getPlayerEntityIds()
for p_id in player_ids:
    p_name = mc.entity.getName(p_id)
    if p_name.lower() == username.lower() or username.lower() in p_name.lower():
        target_id = p_id
        break

if target_id is not None:
    pos = mc.entity.getTilePos(target_id)
    direction = mc.entity.getDirection(target_id)

    # Project direction to horizontal plane (X-Z plane) and normalize
    horizontal_length = math.sqrt(direction.x**2 + direction.z**2)
    if horizontal_length > 0:
        dx = direction.x / horizontal_length
        dz = direction.z / horizontal_length
    else:
        dx, dz = 0.0, 0.0

    # Compute position 4 blocks in front of the player
    bx = int(round(pos.x + 4 * dx))
    by = int(pos.y)
    bz = int(round(pos.z + 4 * dz))

    # The Flying Pig Rain
    from modded.mcpi.entity import PIG
    import random
    import time
    
    spawn_y = pos.y + 30
    print(f"Summoning the Flying Pig Rain above {username}...")
    
    for _ in range(50):
        rx = pos.x + random.uniform(-15, 15)
        rz = pos.z + random.uniform(-15, 15)
        
        eid = mc.spawnEntity(rx, spawn_y, rz, PIG.id)
        if eid:
            # 1200 ticks = 60 seconds
            mc.entity.addPotionEffect(eid, "SLOW_FALLING", 1200, 1)
            
        time.sleep(0.05) # Small delay to make it a continuous rain
        
    print(f"It's raining pigs! Look up!")
else:
    print(f"{username} is not online.")
