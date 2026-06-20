"""
Minecraft Utility Functions

This module provides various utility functions to interact with the Minecraft game world using the RaspberryJuice / modded.mcpi API.

Functions Available:

1. check_is_night_in_game(mc)
   - Usage: is_night = check_is_night_in_game(mc)
   - Description: Checks if it is currently night time in the Minecraft game world. First tries to query the time directly, and falls back to placing a daylight detector if the server doesn't support direct time queries. Returns True if it's night, False otherwise.

2. spawn_mobs_behind_player_at_night(mc, username, mob, duration, interval)
   - Usage: spawn_mobs_behind_player_at_night(mc, "Vincent_Craft3r", ZOMBIE, 60, (5, 10))
   - Description: Continuously checks if it is night and spawns the specified `mob` two blocks behind the player `username`. Runs for `duration` seconds, waiting for a random time between `interval` (min, max) seconds between each check/spawn.

3. print_connected_players(mc)
   - Usage: print_connected_players(mc)
   - Description: Retrieves all connected players' IDs and their current absolute (tile) coordinates and prints them to the console.

4. spawn_skeleton_rider(mc, position)
   - Usage: spawn_skeleton_rider(mc, Vec3(10, 64, 10)) # Or any vector/coordinate tuple
   - Description: Spawns a Skeleton Horse and a Skeleton rider at the specified `position`. Equips the skeleton with custom enchanted Netherite armor and a customized enchanted bow.

5. spawn_zombie_rider(mc, position)
   - Usage: spawn_zombie_rider(mc, Vec3(10, 64, 10))
   - Description: Spawns a Zombie Horse and a Zombie rider at the specified `position`. Equips the zombie with full Netherite armor and a Netherite spear with custom enchantments.

6. make_player_skeleton_rider(mc, username)
   - Usage: make_player_skeleton_rider(mc, "Vincent_Craft3r")
   - Description: Equips the target player with full Netherite armor and a custom enchanted Netherite spear, and mounts the player onto a newly spawned Skeleton Horse.
"""

import time
import math
import datetime
import random

def check_is_night_in_game(mc):
    """
    Checks if it is night in the Minecraft game world.
    First tries to query the time directly (via world.getTime).
    If that's not supported by the server, falls back to placing a daylight detector.
    """
    try:
        # Try direct time query (requires updated RaspberryJuice plugin)
        time_str = mc.conn.sendReceive(b"world.getTime")
        if time_str != "Fail":
            current_time = int(time_str)
            hours = (int(current_time / 1000) + 6) % 24
            minutes = int((current_time % 1000) * 60 / 1000)
            print(f"Current game time: {hours:02d}:{minutes:02d}")
            # In Minecraft, 13000 to 23000 is fully dark night
            return 13000 <= current_time <= 23000
    except Exception:
        pass

    # Fallback to daylight detector method
    try:
        # Find any online player to get coordinate context
        player_ids = mc.getPlayerEntityIds()
        if not player_ids:
            x, z = 0, 0
        else:
            p_pos = mc.entity.getTilePos(player_ids[0])
            x, z = int(p_pos.x), int(p_pos.z)
            
        y = mc.getHeight(x, z)
        test_y = min(y + 10, 255) # Stay within standard world limit
        
        # Place daylight detector (ID 151)
        mc.setBlock(x, test_y, z, 151)
        time.sleep(0.05)
        
        # Read the daylight detector data
        block_info = mc.getBlockWithData(x, test_y, z)
        
        # Clean up by restoring to air (ID 0)
        mc.setBlock(x, test_y, z, 0)
        
        # The block data of a daylight detector is its redstone power output (0 to 15)
        # At night (after sunset), the power output drops to 0.
        return block_info.data == 0
    except Exception as e:
        print(f"Error checking game time: {e}")
        return False


def spawn_mobs_behind_player_at_night(mc, username, mob, duration, interval):
    """
    Spawns a specified mob two blocks behind the player at random intervals,
    only if the player is online and during the night. Runs for the specified duration.

    :param mc: The Minecraft connection object
    :param username: The username of the player (string)
    :param mob: The mob entity description/ID to spawn
    :param duration: Total duration of the period in seconds
    :param interval: Tuple of (min_seconds, max_seconds) for the random sleep interval
    """
    start_time = time.time()
    min_int, max_int = interval

    print(f"Starting {duration}s check and spawn routine for player '{username}'...")
    while time.time() - start_time < duration:
        is_night = check_is_night_in_game(mc)

        if is_night:
            try:
                player_ids = mc.getPlayerEntityIds()
                target_id = None
                for p_id in player_ids:
                    if mc.entity.getName(p_id) == username:
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

                    # Compute position 2 blocks behind him (opposite direction)
                    bx = int(round(pos.x - 2 * dx))
                    by = int(pos.y)  # same level as feet
                    bz = int(round(pos.z - 2 * dz))

                    # Spawn mob
                    entity_id = mc.spawnEntity(bx, by, bz, mob)
                    mob_name = mob.name if hasattr(mob, 'name') else f"ID {mob}"
                    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Spawned {mob_name} (ID {entity_id}) 2 blocks behind {username} at ({bx}, {by}, {bz}).")
                else:
                    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {username} is not online.")
            except Exception as e:
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Error: {e}")
        else:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] It is currently day time. No mob spawned.")

        # Sleep for a random interval within range
        sleep_time = random.uniform(min_int, max_int)
        # Clamp sleep_time to remaining duration
        remaining = duration - (time.time() - start_time)
        if remaining <= 0:
            break
        sleep_time = min(sleep_time, remaining)
        print(f"Sleeping for {sleep_time:.2f}s...")
        time.sleep(sleep_time)

    print("Finished mob spawning period.")


def print_connected_players(mc):
    """
    Prints all connected players with their absolute coordinates.
    """
    try:
        player_ids = mc.getPlayerEntityIds()
        print(f"Connected player IDs: {player_ids}")
        for p_id in player_ids:
            try:
                name = mc.entity.getName(p_id)
                pos = mc.entity.getTilePos(p_id)
                print(f"Player ID: {p_id}, Name: {name}, Position: ({pos.x}, {pos.y}, {pos.z})")
            except Exception as e:
                print(f"Could not retrieve info for ID {p_id}: {e}")
    except Exception as e:
        print(f"Error getting player IDs: {e}")


def spawn_skeleton_rider(mc, position):
    """
    Spawns a skeleton riding a skeleton horse at the specified position.
    """
    try:
        if hasattr(position, "x"):
            bx, by, bz = int(position.x), int(position.y), int(position.z)
        else:
            bx, by, bz = int(position[0]), int(position[1]), int(position[2])
            
        # Spawn skeleton horse
        from modded.mcpi.entity import SKELETON_HORSE, SKELETON
        horse_id = mc.spawnEntity(bx, by, bz, SKELETON_HORSE)
        
        # Spawn skeleton
        skeleton_id = mc.spawnEntity(bx, by, bz, SKELETON)
        
        # Make skeleton ride the horse
        mc.entity.addPassenger(horse_id, skeleton_id)
        
        # Equip skeleton with custom enchanted bow (Flame I, Power V, Punch II, Unbreaking III)
        mc.entity.setEquipment(skeleton_id, "mainhand", "BOW", "flame", 1, "power", 5, "punch", 2, "unbreaking", 3)
        
        # Equip skeleton with Netherite armor
        mc.entity.setEquipment(skeleton_id, "helmet", "NETHERITE_HELMET")
        mc.entity.setEquipment(skeleton_id, "chestplate", "NETHERITE_CHESTPLATE")
        mc.entity.setEquipment(skeleton_id, "leggings", "NETHERITE_LEGGINGS")
        mc.entity.setEquipment(skeleton_id, "boots", "NETHERITE_BOOTS")
        
        print(f"Spawned Skeleton Rider (Skeleton ID {skeleton_id} on Skeleton Horse ID {horse_id}) at ({bx}, {by}, {bz}).")
    except Exception as e:
        print(f"Error spawning skeleton rider: {e}")


def spawn_zombie_rider(mc, position):
    """
    Spawns a zombie riding a zombie horse at the specified position.
    The zombie is equipped with full Netherite armor and a Netherite spear 
    enchanted with Fire Aspect 2, Knockback 2, Lunge 3, Sharpness 5, and Unbreaking 3.
    """
    try:
        if hasattr(position, "x"):
            bx, by, bz = int(position.x), int(position.y), int(position.z)
        else:
            bx, by, bz = int(position[0]), int(position[1]), int(position[2])
            
        # Spawn zombie horse
        from modded.mcpi.entity import ZOMBIE_HORSE, ZOMBIE
        horse_id = mc.spawnEntity(bx, by, bz, ZOMBIE_HORSE)
        
        # Spawn zombie
        zombie_id = mc.spawnEntity(bx, by, bz, ZOMBIE)
        
        # Make zombie ride the horse
        mc.entity.addPassenger(horse_id, zombie_id)
        
        # Equip zombie with custom enchanted Netherite spear
        mc.entity.setEquipment(zombie_id, "mainhand", "NETHERITE_SPEAR", "fire_aspect", 2, "knockback", 2, "lunge", 3, "sharpness", 5, "unbreaking", 3)
        
        # Equip zombie with Netherite armor
        mc.entity.setEquipment(zombie_id, "helmet", "NETHERITE_HELMET")
        mc.entity.setEquipment(zombie_id, "chestplate", "NETHERITE_CHESTPLATE")
        mc.entity.setEquipment(zombie_id, "leggings", "NETHERITE_LEGGINGS")
        mc.entity.setEquipment(zombie_id, "boots", "NETHERITE_BOOTS")
        
        print(f"Spawned Zombie Rider (Zombie ID {zombie_id} on Zombie Horse ID {horse_id}) at ({bx}, {by}, {bz}).")
    except Exception as e:
        print(f"Error spawning zombie rider: {e}")

def make_player_skeleton_rider(mc, username):
    """
    Equips the given player with full Netherite armor and a Netherite spear 
    (like a zombie horseman) and mounts them on a skeleton horse.
    """
    try:
        player_ids = mc.getPlayerEntityIds()
        target_id = None
        for p_id in player_ids:
            p_name = mc.entity.getName(p_id)
            if p_name.lower() == username.lower() or username.lower() in p_name.lower():
                target_id = p_id
                break
                
        if target_id is not None:
            # Equip player with custom enchanted Netherite spear
            mc.entity.setEquipment(target_id, "mainhand", "NETHERITE_SPEAR", "fire_aspect", 2, "knockback", 2, "lunge", 3, "sharpness", 5, "unbreaking", 3)
            
            # Equip player with Netherite armor
            mc.entity.setEquipment(target_id, "helmet", "NETHERITE_HELMET")
            mc.entity.setEquipment(target_id, "chestplate", "NETHERITE_CHESTPLATE")
            mc.entity.setEquipment(target_id, "leggings", "NETHERITE_LEGGINGS")
            mc.entity.setEquipment(target_id, "boots", "NETHERITE_BOOTS")
            
            # Get player position to spawn the skeleton horse
            pos = mc.entity.getTilePos(target_id)
            bx, by, bz = int(pos.x), int(pos.y), int(pos.z)
            
            # Spawn skeleton horse
            from modded.mcpi.entity import SKELETON_HORSE
            horse_id = mc.spawnEntity(bx, by, bz, SKELETON_HORSE)
            
            # Make player ride the horse
            mc.entity.addPassenger(horse_id, target_id)
            
            print(f"Equipped player {username} and mounted them on Skeleton Horse ID {horse_id}.")
        else:
            print(f"Player {username} is not online.")
    except Exception as e:
        print(f"Error equipping/mounting player: {e}")
