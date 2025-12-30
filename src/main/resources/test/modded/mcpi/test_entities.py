from mcpi.minecraft import Minecraft
from mcpi import entity
import time

def main():
    mc = Minecraft.create()
    pos = mc.player.getPos()
    
    # List of new entities to test
    new_mobs = [
        (entity.BEE, "Bee"),
        (entity.PANDA, "Panda"),
        (entity.FOX, "Fox"),
        (entity.ALLAY, "Allay")
    ]

    for mob, name in new_mobs:
        mc.postToChat("Spawning " + name)
        print("Spawning " + name)
        # Spawn 2 blocks away
        mc.spawnEntity(pos.x + 2, pos.y, pos.z, mob)
        time.sleep(2)

if __name__ == "__main__":
    main()
