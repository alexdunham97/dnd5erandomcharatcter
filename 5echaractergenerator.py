import random

races_nathan = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Gnome', 'Half-Elf']
races_normal = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
classes_full_casters = ['Wizard', 'Warlock', 'Cleric', 'Bard', 'Sorcerer', 'Druid']
classes_half_casters = ['Paladin', 'Ranger', 'Fighter', 'Rogue']
classes_non_casters = ['Barbarian', 'Fighter', 'Monk', 'Rogue']


backgrounds = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit', 'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier', 'Urchin']

genders = ['Male', 'Female']

alignments = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Neutral', 'Neutral', 'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']

hair_color = ['Brown', 'Blond', 'Black', 'Red', 'White', 'Blue', 'Gray', 'Other', 'None']

abilities = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']

skills = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight', 'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion', 'Religion', 'Sleight of Hand', 'Stealth', 'Survival']

simple_melee = ['Club', 'Dagger', 'Greatclub', 'Handaxe', 'Javelin', 'Light Hammer', 'Mace', 'Quarterstaff', 'Sickle', 'Spear']
simple_ranged = ['Light Crossbow', 'Dart', 'Shortbow', 'Sling']
martial_melee = ['Battleaxe', 'Flail', 'Glaive', 'Greataxe', 'Greatsword', 'Halberd', 'Lance', 'Longsword', 'Maul', 'Morningstar', 'Pike', 'Rapier', 'Scimitar', 'Shortsword', 'Trident', 'War Pick', 'Warhammer', 'Whip']
martial_ranged = ['Blowgun', 'Hand Crossbow', 'Heavy Crossbow', 'Longbow', 'Net']
simple = simple_melee + simple_ranged
martial = martial_melee + martial_ranged

instruments = ['Bagpipes', 'Drum', 'Dulcimer', 'Flute', 'Lute', 'Lyre', 'Horn', 'Pan flute', 'Shawm', 'Viol']

artisan = ["Alchemist's supplies", "Brewer's supplies", "Calligrapher's supplies", "Carpenter's tools", "Cartographer's tools", "Cobbler's tools", "Cook's utensils", "Glassblower's tools", "Jeweler's tools", "Leatherworker's tools", "Mason's tools", "Painter's supplies", "Potter's supplies", "Smith's tools", "Tinker's tools", "Weaver's tools", "Woodcarver's tools"]
random_simple_melee = random.choice(simple_melee)
random_simple_ranged = random.choice(simple_ranged)
random_martial_melee = random.choice(martial_melee)
random_martial_ranged = random.choice(martial_ranged)
random_simple = random.choice(simple)
random_martial = random.choice(martial)

d4 = [1, 2, 3, 4]
d6 = [1, 2, 3, 4, 5, 6]
d8 = [1, 2, 3, 4, 5, 6, 7, 8]
d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

random_race_normal = random.choice(races_normal)

random_race_nathan = random.choice(races_nathan)

random_class = random.choice(classes)

random_full_cast = random.choice(classes_full_casters)

random_half_cast = random.choice(classes_half_casters)

random_non_cast = random.choice(classes_non_casters)

random_background = random.choice(backgrounds)

random_gender = random.choice(genders)

random_alignment = random.choice(alignments)

random_hair = random.choice(hair_color)

random_ability = random.choice(abilities)

random_skill = random.choice(skills)

random_instrument = random.choice(instruments)

random_artisan = random.choice(artisan)

random_instrument_3 = random.sample(set(instruments), 3)


nathans_campaign = str(raw_input("Is this for Nathan's campaign? Y/N: "))
if nathans_campaign == "Y":
    dumb_death = str(raw_input("Do you need a new character because you died a stupid death? Y/N: "))
    if dumb_death == "Y":
        print "Congrats, you get to play a Kenku!"
    elif dumb_death == "N":
        print 'Still working on the fixing the kinks to this one, sorry!'
    else:
        print "Please just type 'Y' or 'N', it's really not that hard."
elif nathans_campaign == "N":
    if random_race_normal == 'Dwarf':
        race_trait = ['+2 to Con', 'Darkvision up to 60 feet', 'Advantage on saving throws against poison, resistance to poison damage', 'Proficiency with battle/handaxe, throwing/warhammer', "Proficiency with smith's/mason's/brewer's tools/supplies", "Double proficiency bonus to History (Int) checks related to stonework"]
        size = "Medium"
        speed = "25 feet (not reduced by heavy armor)"
        languages = "Common and Dwarvish"
        dwarf_type = random.choice(['Hill', 'Mountain'])
        if dwarf_type == 'Hill':
            base_height = 44
            height_mod = 2 * random.choice(d4)
            total_height = base_height + height_mod
            base_weight = 115
            weight_mod = height_mod * (2 * random.choice(d6))
            total_weight = base_weight + weight_mod
            subrace_trait = ['+1 to Wis', '+1 to HP Max and +1 to HP for every level']
        elif dwarf_type == 'Mountain':
            base_height = 48
            height_mod = 2 * random.choice(d4)
            total_height = base_height + height_mod
            base_weight = 130
            weight_mod = height_mod * (2 * random.choice(d6))
            total_weight = base_weight + weight_mod
            subrace_trait = ['+2 to Str', 'Proficiency with light/medium armor']
    elif random_race_normal == 'Elf':
        race_trait = ['+2 to Dex', 'Darkvision up to 60 feet', "Advantage on saving throws against being charmed, magic can't put you to sleep", 'Proficiency in Perception skill', "Don't need to sleep, 4 hours meditate instead"]
        size = "Medium"
        speed = "30 feet"
        languages = "Common and Elvish"
        elf_type = random.choice(['High', 'Wood', 'Drow'])
        if elf_type == 'High':
            base_height = 54
            height_mod = 2 * random.choice(d10)
            total_height = base_height + height_mod
            base_weight = 90
            weight_mod = height_mod * (random.choice(d4))
            total_weight = base_weight + weight_mod
            subrace_trait = ['+1 to Int', 'Proficiency with long/short sword/bow', 'Know 1 cantrip from Wizard spell list, use Int', 'Add 1 extra language']
        elif elf_type == 'Wood':
            base_height = 54
            height_mod = 2 * random.choice(d10)
            total_height = base_height + height_mod
            base_weight = 100
            weight_mod = height_mod * (random.choice(d4))
            total_weight = base_weight + weight_mod
            subrace_trait = ['+1 to Wis', 'Proficiency with long/short sword/bow', 'Base speed is now 35 feet', 'You can attempt to hide even when only lightly obscured']
        elif elf_type == 'Drow':
            base_height = 53
            height_mod = 2 * random.choice(d6)
            total_height = base_height + height_mod
            base_weight = 75
            weight_mod = height_mod * (random.choice(d6))
            total_weight = base_weight + weight_mod
            subrace_trait = ['+1 to Cha', 'Darkvision increased to 120 feet', 'Disadvantage on attack and Wisdom (Perception) checks that rely on sight in direct sunlight', "Know 'Dancing Lights' cantrip; at level 3 you can cast 'Faerie Fire' once per day; at level 5, you can cast 'Darkness' once per day; use Cha", 'Proficiency with rapiers, shortswords, and hand crossbows']
    elif random_race_normal == "Halfling":
        race_trait = ['+2 to Dex', 'You can re-roll a 1 on attack roll, ability check, or saving throw', "Advantage on saving throws against being frightened", 'You can move through space of any creature that is larger than you']
        size = "Small"
        speed = "25 feet"
        languages = "Common and Halfling"
        base_height = 31
        height_mod = 2 * random.choice(d4)
        total_height = base_height + height_mod
        base_weight = 35
        weight_mod = height_mod
        total_weight = base_weight + weight_mod
        halfling_type = random.choice(['Lightfoot', 'Stout'])
        if halfling_type == 'Lightfoot':
            subrace_trait = ['+1 to Cha', 'You can attempt to hide even when you are obscured only by a creature that is larger than you']
        elif halfling_type == 'Stout':
            subrace_trait = ['+1 to Con', 'Advantage on saving throws against poison, resistance to poison damage']
    elif random_race_normal == "Human":
        race_trait = ['+1 to every stat']
        size = "Medium"
        speed = "30 feet"
        languages = "Common and 1 other language"
        base_height = 56
        height_mod = 2 * random.choice(d10)
        total_height = base_height + height_mod
        base_weight = 110
        weight_mod = height_mod * (2 * random.choice(d4))
        total_weight = base_weight + weight_mod
    elif random_race_normal == "Dragonborn":
        race_trait = ['+2 to Str, +1 to Cha', 'Breath Weapon', "Resistance to damage type associated with draconic ancestry"]
        size = "Medium"
        speed = "30 feet"
        languages = "Common and Draconic"
        draconic_ancestry = random.choice(['Black (acid)', 'Blue (lightning)', 'Brass (fire)', 'Bronze (lightning)', 'Copper (acid)', 'Gold (fire)', 'Green (poison)', 'Red (fire)', 'Silver (cold)', 'White (cold)'])
        base_height = 66
        height_mod = 2 * random.choice(d8)
        total_height = base_height + height_mod
        base_weight = 175
        weight_mod = height_mod * (2 * random.choice(d6))
        total_weight = base_weight + weight_mod
    elif random_race_normal == "Gnome":
        race_trait = ['+2 to Int', 'Darkvision up to 60 feet', "Advantage on all Int, Wis, and Cha saving throws against magic"]
        size = "Small"
        speed = "25 feet"
        languages = "Common and Gnomish"
        base_height = 35
        height_mod = 2 * random.choice(d4)
        total_height = base_height + height_mod
        base_weight = 35
        weight_mod = height_mod
        total_weight = base_weight + weight_mod
        gnome_type = random.choice(['Forest', 'Rock'])
        if gnome_type == 'Forest':
            subrace_trait = ['+1 to Dex', "You know 'Minor Illusion' cantrip, use Int", 'You can communicate simple ideas with Small or smaller beasts through sounds and simple gestures']
        elif gnome_type == 'Rock':
            subrace_trait = ['+1 to Con', 'Double proficiency bonus to History (Int) checks related to magic/alchemical/technological items', "Proficiency with artisan's tools; you can spend 1 hour and 10 gp worth of materials to construct tiny clockwork device; you can have 3 at a time; lasts for 24 hours or until dismantled"]
    elif random_race_normal == "Half-Elf":
        race_trait = ['+2 to Cha, +1 to 2 other abilities', 'Darkvision up to 60 feet', "Advantage on saving throws against being charmed, magic can't put you to sleep", 'Proficiency in 2 skills of choice']
        size = "Medium"
        speed = "30 feet"
        languages = "Common and Elvish and 1 other language"
        base_height = 57
        height_mod = 2 * random.choice(d8)
        total_height = base_height + height_mod
        base_weight = 110
        weight_mod = height_mod * (2 * random.choice(d4))
        total_weight = base_weight + weight_mod
    elif random_race_normal == "Half-Orc":
        race_trait = ['+2 to Str, +1 to Con', 'Darkvision up to 60 feet', 'You can drop to 1 hp instead of 0 hp (unless killed outright); once per long rest', 'Proficiency in Intimidation skill', "When you score a critical hit (melee), you can roll one of the weapon's damage dice 1 additional time and add it to the damage of the critical hit"]
        size = "Medium"
        speed = "30 feet"
        languages = "Common and Orc"
        base_height = 58
        height_mod = 2 * random.choice(d10)
        total_height = base_height + height_mod
        base_weight = 140
        weight_mod = height_mod * (2 * random.choice(d6))
        total_weight = base_weight + weight_mod
    elif random_race_normal == "Tiefling":
        race_trait = ['+2 to Cha, +1 to Int', 'Darkvision up to 60 feet', 'Resistance to fire damage', "Know 'Thaumaturgy' cantrip; at level 3 you can cast 'Hellish Rebuke' once per day as level 2 spell slot; at level 5, you can cast 'Darkness' once per day; use Cha" ]
        size = "Medium"
        speed = "30 feet"
        languages = "Common and Infernal"
        base_height = 57
        height_mod = 2 * random.choice(d8)
        total_height = base_height + height_mod
        base_weight = 110
        weight_mod = height_mod * (2 * random.choice(d4))
        total_weight = base_weight + weight_mod


    if random_class == "Barbarian":
        subclass = ['Berserker', 'Totem Warrior', 'Ancestral Guardian', 'Storm Herald', 'Zealot']
        random_subclass = random.choice(subclass)
        armor_prof = "Light/medium, shields"
        weapon_prof = "Simple/martial"
        tool_prof = "None"
        saving_throw_prof = "Str/Con"
        skill_prof = random.sample(set(['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival']), 2)
        equipment = ["Explorer's pack", 'Four Javelins']
        equipment.append(random.choice(['Greataxe', random_martial_melee]))
        equipment.append(random.choice(['Two Handaxes', random_simple]))

    elif random_class == "Bard":
        subclass = ['Lore', 'Valor', 'Glamour', 'Swords', 'Whispers']
        random_subclass = random.choice(subclass)
        armor_prof = "Light"
        weapon_prof = "Simple weapons, hand crossbows, longswords, rapiers, shortswords"
        tool_prof = random_instrument_3
        saving_throw_prof = "Dex/Cha"
        skill_prof = random.sample(set(skills), 3)
        equipment = ["Leather armor", 'Dagger']
        equipment.append(random.choice(['Rapier', 'Longsword', random_simple]))
        equipment.append(random.choice(["Diplomat's pack", "Entertainer's pack"]))
        equipment.append(random.choice(['Lute', random.choice(tool_prof)]))

    elif random_class == "Cleric":
        subclass = ['Knowledge', 'Life', 'Light', 'Nature', 'Tempest', 'Trickery', 'War', 'Forge', 'Grave']
        random_subclass = random.choice(subclass)
        armor_prof = "Light/medium, shields"
        weapon_prof = "Simple"
        tool_prof = "None"
        saving_throw_prof = "Wis/Cha"
        skill_prof = random.sample(set(['History', 'Insight', 'Medicine', 'Persuasion', 'Religion']), 2)
        equipment = ["Shield", 'Holy symbol']
        equipment.append(random.choice(['Mace', 'Warhammer (if not proficient, then Mace)']))
        equipment.append(random.choice(['Scale mail', 'Leather armor', 'Chain mail (if not proficient, then Scale mail or Leather armor)']))
        equipment.append(random.choice(['Light crossbow and 20 bolts', random_simple]))
        equipment.append(random.choice(["Priest's pack", "Explorer's pack"]))

    elif random_class == "Druid":
        subclass = ['the Land', 'the Moon', 'Dreams', 'the Shepherd']
        random_subclass = random.choice(subclass)
        armor_prof = "Light/medium, shields (non-metal)"
        weapon_prof = "Clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears"
        tool_prof = "Herbalism kit"
        saving_throw_prof = "Int/Wis"
        skill_prof = random.sample(set(['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival']), 2)
        equipment = ["Leather armor", "Explorer's pack", 'Druidic focus']
        equipment.append(random.choice(['Wooden shield', random_simple]))
        equipment.append(random.choice(["Scimitar", random_simple_melee]))


    elif random_class == "Fighter":
        subclass = ['Champion', 'Battle Master', 'Eldritch Knight', 'Arcane Archer', 'Cavalier', 'Samurai']
        random_subclass = random.choice(subclass)
        armor_prof = "All armor, shields"
        weapon_prof = "Simple weapons, martial weapons"
        tool_prof = 'None'
        saving_throw_prof = "Str/Con"
        skill_prof = random.sample(set(['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']), 2)
        equipment = []
        equipment.append(random.choice(['Chain mail', 'Leather armor, longbow and 20 arrows']))
        equipment.append(random.choice([random_martial+" and Shield", random.sample(set(martial), 2)]))
        equipment.append(random.choice(['Light crossbow and 20 bolts', 'Two Handaxes']))
        equipment.append(random.choice(["Dungeoneer's pack", "Explorer's pack"]))


    elif random_class == "Monk":
        subclass = ['the Open Hand', 'Shadow', 'the Four Elements', 'the Drunken Master', 'the Kensei', 'the Sun Soul']
        random_subclass = random.choice(subclass)
        armor_prof = "None"
        weapon_prof = "Simple weapons, shortswords"
        tool_prof = random.choice([random_artisan, random_instrument])
        saving_throw_prof = "Str/Dex"
        skill_prof = random.sample(set(['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth']), 2)
        equipment = ['10 darts']
        equipment.append(random.choice(['Shortsword', random_simple]))
        equipment.append(random.choice(["Dungeoneer's pack", "Explorer's pack"]))

    elif random_class == "Paladin":
        subclass = ['of Devotion', 'of the Ancients', 'of Vengeance', 'Breaker', 'of Conquest', 'of Redemption']
        random_subclass = random.choice(subclass)
        armor_prof = "All armor, shields"
        weapon_prof = "Simple weapons, martial weapons"
        tool_prof = "None"
        saving_throw_prof = "Wis/Cha"
        skill_prof = random.sample(set(['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion']), 2)
        equipment = ["Chain mail", 'Holy symbol']
        equipment.append(random.choice(['Five Javelins', random_simple_melee]))
        equipment.append(random.choice([random_martial+" and Shield", random.sample(set(martial), 2)]))
        equipment.append(random.choice(["Priest's pack", "Explorer's pack"]))

    elif random_class == "Ranger":
        subclass = ['Hunter', 'Beastmaster', 'Gloom Stalker', 'Horizon Walker', 'Monster Slayer']
        random_subclass = random.choice(subclass)
        armor_prof = "Light/medium, shields"
        weapon_prof = "Simple weapons, martial weapons"
        tool_prof = "None"
        saving_throw_prof = "Str/Dex"
        skill_prof = random.sample(set(['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival']), 3)
        equipment = ["Longbow and quiver with 20 arrows"]
        equipment.append(random.choice(['Scale mail', 'Leather armor']))
        equipment.append(random.choice(["Two Shortswords", random.sample(set(simple_melee), 2)]))
        equipment.append(random.choice(["Dungeoneer's pack", "Explorer's pack"]))

    elif random_class == "Rogue":
        subclass = ['Thief', 'Assassin', 'Arcane Trickster', 'Mastermind', 'Scout', 'Swashbuckler']
        random_subclass = random.choice(subclass)
        armor_prof = "Light"
        weapon_prof = "Simple weapons, hand crossbows, longswords, rapiers, shortswords"
        tool_prof = "Thieve's tools"
        saving_throw_prof = "Dex/Int"
        skill_prof = random.sample(set(['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth  ']), 4)
        equipment = ["Leather armor", 'Two Daggers', "Thieves' tools"]
        equipment.append(random.choice(['Rapier', 'Shortsword']))
        equipment.append(random.choice(['Shortbow and quiver with 20 arrows', "Shortsword"]))
        equipment.append(random.choice(["Burglar's pack", "Dungeoneer's pack", "Explorer's pack"]))


    elif random_class == "Sorcerer":
        subclass = ['Draconic Bloodline', 'Wild Magic', 'Divine Soul', 'Shadow Magic', 'Storm Sorcery']
        random_subclass = random.choice(subclass)
        armor_prof = "None"
        weapon_prof = "Daggers, darts, slings, quarterstaffs, light crossbows"
        tool_prof = "None"
        saving_throw_prof = "Con/Cha"
        skill_prof = random.sample(set(['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion']), 2)
        equipment = ['Two Daggers']
        equipment.append(random.choice(['Light crossbow and 20 bolts', random_simple]))
        equipment.append(random.choice(["Component pouch", "Arcane focus"]))
        equipment.append(random.choice(["Dungeoneer's pack", "Explorer's pack"]))

    elif random_class == "Warlock":
        subclass = ['Archfey', 'Fiend', 'Great Old One', 'Celestial', 'Hexblade']
        random_subclass = random.choice(subclass)
        armor_prof = "Light"
        weapon_prof = "Simple weapons"
        tool_prof = "None"
        saving_throw_prof = "Wis/Cha"
        skill_prof = random.sample(set(['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion']), 2)
        equipment = ["Leather armor", random_simple, 'Two Daggers']
        equipment.append(random.choice(['Light crossbow and 20 bolts', random_simple]))
        equipment.append(random.choice(['Component pouch', 'Arcane focus']))
        equipment.append(random.choice(["Scholar's pack", "Dungeoneer's pack"]))


    elif random_class == "Wizard":
        subclass = ['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation', 'War Magic']
        random_subclass = random.choice(subclass)
        armor_prof = "None"
        weapon_prof = "Daggers, darts, slings, quarterstaffs, light crossbows"
        tool_prof = "None"
        saving_throw_prof = "Int/Wis"
        skill_prof = random.sample(set(['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion']), 2)
        equipment = ['Spellbook']
        equipment.append(random.choice(['Quarterstaff', 'Dagger']))
        equipment.append(random.choice(['Component pouch', 'Arcane focus']))
        equipment.append(random.choice(["Scholar's pack", "Explorer's pack"]))




    height_feet = total_height/12
    height_inches = total_height - (height_feet * 12)

    print "Gender:", random_gender
    print "Race:", random_race_normal
    if random_race_normal == "Dwarf":
        print "Subrace:", dwarf_type
    elif random_race_normal == "Elf":
        print "Subrace:", elf_type
    elif random_race_normal == "Halfling":
        print "Subrace:", halfling_type
    elif random_race_normal == "Gnome":
        print "Subrace:", gnome_type

    print "Class:", random_class

    if random_class == "Barbarian":
        print "Subclass: Path of the", random_subclass
    elif random_class == "Bard":
        print "Subclass: College of", random_subclass
    elif random_class == "Cleric":
        print "Subclass:",random_subclass,"Domain"
    elif random_class == "Druid":
        print "Subclass: Circle of", random_subclass
    elif random_class == "Monk":
        print "Subclass: Way of", random_subclass
    elif random_class == "Paladin":
        print "Subclass: Oath", random_subclass
    elif random_class == "Warlock":
        print "Subclass: The", random_subclass

    if random_class == ("Fighter" or "Ranger" or "Rogue" or "Sorcerer" or "Wizard"):
        print "Subclass:", random_subclass

    print "Background:", random_background
    if random_race_normal == "Dragonborn":
        print "Dragon ancestor:", draconic_ancestry
    print "Height:", height_feet, "feet", height_inches, "inches"
    print "Weight:", total_weight, "pounds"
    print "Alignment:", random_alignment
    print "Hair color:", random_hair
    print "Size:", size
    print "Speed:", speed
    print "Languages:", languages
    for trait in race_trait:
        print "Racial Trait:", trait

    if random_race_normal == ('Dwarf' or 'Elf' or 'Halfling' or 'Gnome'):
        for sub_trait in subrace_trait:
            print "Sub-racial Trait:", sub_trait

    print "Armor Proficiencies:", armor_prof
    print "Weapon Proficiencies:", weapon_prof
    print "Tool Proficiencies:", tool_prof
    print "Saving Throw Proficiencies:", saving_throw_prof
    for profff in skill_prof:
        print "Skill Proficiencies:", profff
    for thing in equipment:
        print "Equipment:", thing
else:
    print "Jesus how hard is it to write 'Y' or 'N'?"
