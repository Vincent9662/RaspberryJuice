package net.zhuoweizhang.raspberryjuice;

import org.bukkit.Material;
import java.util.HashMap;
import java.util.Map;

public class BlockIdMapper {
    private static final Map<Integer, Material> idToMaterial = new HashMap<>();
    private static final Map<Material, Integer> materialToId = new HashMap<>();

    static {
        register(0, Material.AIR);
        register(1, Material.STONE);
        register(2, Material.GRASS_BLOCK);
        register(3, Material.DIRT);
        register(4, Material.COBBLESTONE);
        register(5, Material.OAK_PLANKS);
        register(6, Material.OAK_SAPLING);
        register(7, Material.BEDROCK);
        register(8, Material.WATER);
        register(9, Material.WATER);
        register(10, Material.LAVA);
        register(11, Material.LAVA);
        register(12, Material.SAND);
        register(13, Material.GRAVEL);
        register(14, Material.GOLD_ORE);
        register(15, Material.IRON_ORE);
        register(16, Material.COAL_ORE);
        register(17, Material.OAK_LOG);
        register(18, Material.OAK_LEAVES);
        register(20, Material.GLASS);
        register(21, Material.LAPIS_ORE);
        register(22, Material.LAPIS_BLOCK);
        register(24, Material.SANDSTONE);
        register(26, Material.RED_BED);
        register(27, Material.POWERED_RAIL);
        register(28, Material.DETECTOR_RAIL);
        register(30, Material.COBWEB);
        register(31, Material.TALL_GRASS);
        register(32, Material.DEAD_BUSH);
        register(35, Material.WHITE_WOOL);
        register(37, Material.DANDELION);
        register(38, Material.BLUE_ORCHID);
        register(39, Material.BROWN_MUSHROOM);
        register(40, Material.RED_MUSHROOM);
        register(41, Material.GOLD_BLOCK);
        register(42, Material.IRON_BLOCK);
        register(43, Material.SMOOTH_STONE_SLAB);
        register(44, Material.SMOOTH_STONE_SLAB);
        register(45, Material.BRICKS);
        register(46, Material.TNT);
        register(47, Material.BOOKSHELF);
        register(48, Material.MOSSY_COBBLESTONE);
        register(49, Material.OBSIDIAN);
        register(50, Material.TORCH);
        register(51, Material.FIRE);
        register(53, Material.OAK_STAIRS);
        register(54, Material.CHEST);
        register(56, Material.DIAMOND_ORE);
        register(57, Material.DIAMOND_BLOCK);
        register(58, Material.CRAFTING_TABLE);
        register(60, Material.FARMLAND);
        register(61, Material.FURNACE);
        register(62, Material.FURNACE);
        register(63, Material.OAK_SIGN);
        register(64, Material.OAK_DOOR);
        register(65, Material.LADDER);
        register(66, Material.RAIL);
        register(67, Material.COBBLESTONE_STAIRS);
        register(68, Material.OAK_WALL_SIGN);
        register(71, Material.IRON_DOOR);
        register(73, Material.REDSTONE_ORE);
        register(76, Material.REDSTONE_TORCH);
        register(78, Material.SNOW);
        register(79, Material.ICE);
        register(80, Material.SNOW_BLOCK);
        register(81, Material.CACTUS);
        register(82, Material.CLAY);
        register(83, Material.SUGAR_CANE);
        register(85, Material.OAK_FENCE);
        register(86, Material.CARVED_PUMPKIN);
        register(87, Material.NETHERRACK);
        register(88, Material.SOUL_SAND);
        register(89, Material.GLOWSTONE);
        register(91, Material.JACK_O_LANTERN);
        register(95, Material.WHITE_STAINED_GLASS);
        register(96, Material.OAK_TRAPDOOR);
        register(98, Material.STONE_BRICKS);
        register(102, Material.GLASS_PANE);
        register(103, Material.MELON);
        register(107, Material.OAK_FENCE_GATE);
        register(108, Material.BRICK_STAIRS);
        register(109, Material.STONE_BRICK_STAIRS);
        register(110, Material.MYCELIUM);
        register(112, Material.NETHER_BRICKS);
        register(113, Material.NETHER_BRICK_FENCE);
        register(114, Material.NETHER_BRICK_STAIRS);
        register(121, Material.END_STONE);
        register(126, Material.OAK_SLAB);
        register(128, Material.SANDSTONE_STAIRS);
        register(129, Material.EMERALD_ORE);
        register(151, Material.DAYLIGHT_DETECTOR);
        register(157, Material.ACTIVATOR_RAIL);
        register(161, Material.DARK_OAK_LEAVES);
        register(167, Material.IRON_TRAPDOOR);
        register(188, Material.SPRUCE_FENCE);
        register(189, Material.BIRCH_FENCE);
        register(190, Material.JUNGLE_FENCE);
        register(191, Material.DARK_OAK_FENCE);
        register(192, Material.ACACIA_FENCE);
        register(193, Material.SPRUCE_DOOR);
        register(194, Material.BIRCH_DOOR);
        register(195, Material.JUNGLE_DOOR);
        register(196, Material.ACACIA_DOOR);
        register(197, Material.DARK_OAK_DOOR);
        register(246, Material.OBSIDIAN);
        register(247, Material.COBBLESTONE);
    }

    private static void register(int id, Material material) {
        idToMaterial.put(id, material);
        if (!materialToId.containsKey(material)) {
            materialToId.put(material, id);
        }
    }

    public static Material getMaterialFromId(int id) {
        Material material = idToMaterial.get(id);
        return material != null ? material : Material.AIR;
    }

    public static int getIdFromMaterial(Material material) {
        Integer id = materialToId.get(material);
        return id != null ? id : 0;
    }
}
