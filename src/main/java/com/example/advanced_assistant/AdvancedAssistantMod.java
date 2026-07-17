package com.example.advanced_assistant;

import net.neoforged.api.distmarker.Dist;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.ModContainer;
import net.neoforged.fml.common.Mod;
import net.neoforged.neoforge.registries.DeferredRegister;
import net.neoforged.neoforge.registries.NeoForgeRegistries;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;

@Mod(AdvancedAssistantMod.MOD_ID)
public class AdvancedAssistantMod {
    public static final String MOD_ID = "advanced_assistant";
    
    // 创建创造模式标签
    public static final CreativeModeTab ADVANCED_TAB = CreativeModeTab.builder()
            .icon(() -> new Item.Properties().stacksTo(1))
            .title(Component.translatable("itemGroup." + MOD_ID))
            .displayItems((pParameters, pOutput) -> {
                // 这里可以添加物品到创造模式标签
            })
            .build();
    
    public AdvancedAssistantMod(IEventBus modEventBus, ModContainer modContainer) {
        // 注册模组内容
        modEventBus.addListener(this::registerEvents);
    }
    
    private void registerEvents() {
        // 注册模组事件
        System.out.println("高级模组助手已加载！");
    }
}