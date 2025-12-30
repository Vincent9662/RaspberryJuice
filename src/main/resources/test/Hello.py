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

# #Modded Library Tests
mc = minecraftmodded.Minecraft.create("172.16.1.4")

# Get the position of player "Salsa_Craft3r"
# salsa_pos = mc.entity.getTilePos(mc.getPlayerEntityId("Salsa_Craft3r"))
# tango_pos = mc.entity.getTilePos(mc.getPlayerEntityId("Tango_Craft3r"))

# Calculate spawn position 3 blocks in front of player V
# We'll spawn it in front based on their direction
# spawn_x = player_pos.x + 3
# spawn_y = player_pos.y
# spawn_z = player_pos.z

# Post a message to chat
# mc.postToChat(f"[-Salsa_Craft3r, your position is at {salsa_pos.x}, {salsa_pos.y}, {salsa_pos.z}-]")
# mc.postToChat(f"[-Tango_Craft3r, your position is at {tango_pos.x}, {tango_pos.y}, {tango_pos.z}-]")

# World-level (absolute coordinates)
# mc.strikeLightning(43, 134, 25)
# mc.strikeLightningEffect(43, 134, 22)

# Player-level (relative to player)
# mc.player.strikeLightning(5, -6, 5)  # 5 blocks away
# mc.player.strikeLightningAtSelf()    # At player location


pos = mc.player.getPos()

# # List of new entities to test
# new_mobs = [
#     (entitymodded.BEE, "Bee"),
#     (entitymodded.PANDA, "Panda"),
#     (entitymodded.FOX, "Fox"),
#     (entitymodded.ALLAY, "Allay")
# ]

# hustle_mobs = [
#     # (entitymodded.WARDEN, "Warden"),
#     (entitymodded.PHANTOM, "Phantom"),
#     (entitymodded.ZOGLIN, "Zombie Piglin"),
#     (entitymodded.BOGGED, "Bogged")


# for mob, name in hustle_mobs:
#     mc.postToChat("Spawning " + name)
#     print("Spawning " + name)
#     # Spawn 2 blocks away
#     mc.spawnEntity(pos.x + 2, pos.y, pos.z, mob)
#     time.sleep(2)

# try:
#     while True:
#         target = mc.player.getTileLookingAt()
#         mc.strikeLightning(target.x, target.y, target.z)
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     print("Stopped.")

target = mc.player.getTileLookingAt()
print(pos)
print(target)



