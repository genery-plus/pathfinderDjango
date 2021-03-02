# from django.conf import settings
from django.db import models
# from django.utils import timezone

class character(models.Model):
    #description - описание
    character_name = models.TextField()
    worldview = models.TextField()
    nameperson = models.TextField()
    lvlcharacter = models.TextField()
    thedeity = models.TextField()
    homeland = models.TextField()
    race = models.TextField()
    size = models.TextField()
    floor = models.TextField()
    age = models.TextField()
    height = models.TextField()
    weight = models.TextField()
    hair = models.TextField()
    eye = models.TextField()
    #abilities - характеристики
    srtength_ability_score = models.TextField()
    srtength_ability_modifier = models.TextField()
    srtength_temp_adjustment = models.TextField()
    srtength_temp_modifier= models.TextField()
    dexterity_ability_score = models.TextField()
    dexterity_ability_modifier = models.TextField()
    dexterity_temp_adjustment = models.TextField()
    dexterity_temp_modifier = models.TextField()
    constitution_ability_score = models.TextField()
    constitution_ability_modifier = models.TextField()
    constitution_temp_adjustment = models.TextField()
    constitution_temp_modifier  = models.TextField()
    intelligence_ability_score = models.TextField()
    intelligence_ability_modifier = models.TextField()
    intelligence_temp_adjustment = models.TextField()
    intelligence_temp_modifier = models.TextField()
    wisdom_ability_score = models.TextField()
    wisdom_ability_modifier= models.TextField()
    wisdom_temp_adjustment = models.TextField()
    wisdom_temp_modifier = models.TextField()
    charisma_ability_score = models.TextField()
    charisma_ability_modifier= models.TextField()
    charisma_temp_adjustment = models.TextField()
    charisma_temp_modifier = models.TextField()
    #armor-класс брони
    armor_class_total = models.TextField()
    armor_class_bonus = models.TextField()
    armor_class_shield_bonus = models.TextField()
    armor_class_dex_modifier = models.TextField()
    armor_class_size_modifier = models.TextField()
    armor_class_natural_armor = models.TextField()
    armor_class_deflection_modifier = models.TextField()
    armor_class_misc_modifier = models.TextField()
    touch_armor_class = models.TextField()
    flat_footed_armor_class = models.TextField()
    armor_class_modifier  = models.TextField()
    #HP - здоровье
    hit_points_total = models.TextField()
    hit_points_damage_reduction = models.TextField()
    hit_points_wounds_current_HP = models.TextField()
    hit_points_nonlethal_damage = models.TextField()
    #инициативы
    initiative_modifier_total = models.TextField()
    initiative_modifier_dex_modifier = models.TextField()
    initiative_modifier_misc_modifier = models.TextField()
    #наземная скорость
    speed_land_base_speed_FT_SQ = models.TextField()
    speed_land_with_armor_FT_SQ = models.TextField()
    speed_land_fly_FT = models.TextField()
    speed_land_maneuverability_FT = models.TextField()
    speed_land_swim_FT = models.TextField()
    speed_land_climb_FT = models.TextField()
    speed_land_burrow_FT = models.TextField()
    speed_land_temp_modifiers = models.TextField()
    #испытания
    fortitude_total =  models.TextField() #стойкость
    fortitude_base_save = models.TextField()  #стойкость
    fortitude_ability_modifier = models.TextField()  #стойкость
    fortitude_magic_modifier = models.TextField()  #стойкость
    fortitude_misc_modifier = models.TextField()  #стойкость
    fortitude_temporary_modifier = models.TextField()  #стойкость
    reflex_total = models.TextField() #реакция
    reflex_base_save = models.TextField()  # реакция
    reflex_ability_modifier = models.TextField()  # реакция
    reflex_magic_modifier = models.TextField()  # реакция
    reflex_misc_modifier = models.TextField()  # реакция
    reflex_temporary_modifier = models.TextField()  # реакция
    will_total = models.TextField()  # воля
    will_base_save = models.TextField()  #воля
    will_ability_modifier = models.TextField()  # воля
    will_magic_modifier = models.TextField()  # воля
    will_misc_modifier = models.TextField()  # воля
    will_temporary_modifier = models.TextField()  # воля
    saving_throws_modifier = models.TextField() #общая модель для всех испытаний
    #other
    base_attack_bonus = models.TextField()
    spell_resistance = models.TextField()
    #cmb
    cmb_total = models.TextField()
    cmb_base_attack_bonus = models.TextField()
    cmb_strength_modifier = models.TextField()
    cmb_size_modifier = models.TextField()
    cmb_modifier = models.TextField()
    #cmd
    cmd_total = models.TextField()
    cmd_base_attack_bonus = models.TextField()
    cmd_strength_modifier = models.TextField()
    cmd_dexterity_modifier = models.TextField()
    cmd_size_modifier = models.TextField()
    #weapon_one
    weapon_one_name = models.TextField()
    weapon_one_attack_bonus = models.TextField()
    weapon_one_critical = models.TextField()
    weapon_one_type = models.TextField()
    weapon_one_range = models.TextField()
    weapon_one_ammunition = models.TextField()
    weapon_one_damage = models.TextField()
    #weapon_two
    weapon_two_name = models.TextField()
    weapon_two_attack_bonus = models.TextField()
    weapon_two_critical = models.TextField()
    weapon_two_type = models.TextField()
    weapon_two_range = models.TextField()
    weapon_two_ammunition = models.TextField()
    weapon_two_damage = models.TextField()
    #weapon_three
    weapon_three_name = models.TextField()
    weapon_three_attack_bonus = models.TextField()
    weapon_three_critical = models.TextField()
    weapon_three_type = models.TextField()
    weapon_three_range = models.TextField()
    weapon_three_ammunition = models.TextField()
    weapon_three_damage = models.TextField()
    #weapon_four
    weapon_four_name = models.TextField()
    weapon_four_attack_bonus = models.TextField()
    weapon_four_critical = models.TextField()
    weapon_four_type = models.TextField()
    weapon_four_range = models.TextField()
    weapon_four_ammunition = models.TextField()
    weapon_four_damage = models.TextField()
    #weapon_five
    weapon_five_name = models.TextField()
    weapon_five_attack_bonus = models.TextField()
    weapon_five_critical = models.TextField()
    weapon_five_type = models.TextField()
    weapon_five_range = models.TextField()
    weapon_five_ammunition = models.TextField()
    weapon_five_damage = models.TextField()
    #skills
    skill_acrobatics_total_bonus = models.TextField() #1
    skill_acrobatics_ranks = models.TextField()
    skill_acrobatics_misc_mod = models.TextField()
    skill_acrobatics_class_skill = models.TextField()
    skill_acrobatics_trained_only = models.TextField()
    skill_appraise_total_bonus = models.TextField() #2
    skill_appraise_ranks = models.TextField()
    skill_appraise_misc_mod = models.TextField()
    skill_appraise_class_skill = models.TextField()
    skill_appraise_trained_only = models.TextField()
    skill_bluff_total_bonus = models.TextField() #3
    skill_bluff_ranks = models.TextField()
    skill_bluff_misc_mod = models.TextField()
    skill_bluff_class_skill = models.TextField()
    skill_bluff_trained_only = models.TextField()






