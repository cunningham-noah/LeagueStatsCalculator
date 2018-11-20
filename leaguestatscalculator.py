'''Attribute List:
   HP, HP_Plus, HP5, HP5_Plus, MP, MP_Plus, MP5, MP5_Plus, Armor, Armor_Plus, MR, MR_Plus, Move_Speed, Life_Steal, 
   Lethality, Armor_Pen, Magic_Pen, Crit_Chance, AS, AS_Plus (Percentage), AD, AD_Plus, AP, AP_Plus, CDR, En, EnP5'''
   
champions = {
	"Aatrox":
		{"HP":580, "HP_Plus":80, "HP5":5, "HP5_Plus":0.25, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":33, "Armor_Plus":3.25, "MR":32.1, "MR_Plus":1.25,
		"Move_Speed":345, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0.651, "AS_Plus":0.025 "AD":60, "AD_Plus":5, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Ahri":
		{"HP":526, "HP_Plus":92, "HP5":6.5, "HP5_Plus":0.6, "MP":418, "MP_Plus":25, "MP5":8, "MP5_Plus":0.8, "Armor":20.88, "Armor_Plus":3.5, "MR":30, "MR_Plus":0.5,
		"Move_Speed":330, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0.668, "AS_Plus":0.02, "AD":53.04, "AD_Plus":3, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Akali":
		{"HP":550, "HP_Plus":85, "HP5":3.5, "HP5_Plus":0.5, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":23, "Armor_Plus":3.5, "MR":32.1, "MR_Plus":1.25,
		"Move_Speed":345, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0.625, "AS_Plus":0.032, "AD":62.4, "AD_Plus":3.3, "AP":0, "AP_Plus":0,
		"CDR":0, "En":200, "EnP5":50},
	"Alistar":
		{"HP":573.36, "HP_Plus":106, "HP5":8.5, "HP5_Plus":0.85, "MP":278.84, "MP_Plus":38, "MP5":8.5, "MP5_Plus":0.8, "Armor":44, "Armor_Plus":3.5, "MR":32.1, "MR_Plus":1.25,
		"Move_Speed":330, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0.625, "AS_Plus":0.02125, "AD":61.112, "AD_Plus":3.62, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Amumu":
		{"HP":613.12, "HP_Plus":84, "HP5":9, "HP5_Plus":0.85, "MP":287.2, "MP_Plus":40, "MP5":7.382, "MP5_Plus":0.525, "Armor":33, "Armor_Plus":3.8, "MR":32.1, "MR_Plus":1.25,
		"Move_Speed":335, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0.638, "AS_Plus":'''15.3+2.18%''', "AD":53.38, "AD_Plus":3.8, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Anivia":
		{"HP":480, "HP_Plus":82, "HP5":5.5, "HP5_Plus":0.55, "MP":495, "MP_Plus":25, "MP5":8, "MP5_Plus":0.8, "Armor":21.22, "Armor_Plus":4, "MR":30, "MR_Plus":0.5,
		"Move_Speed":325, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0.625, "AS_Plus":0.0168, "AD":51.376, "AD_Plus":3.2, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Annie":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Ashe":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Aurelion Sol":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Azir":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Bard":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Blitzcrank":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Brand":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Braum":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Caitlyn":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Camille":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Cassiopeia":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Cho'Gath":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Corki":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Darius":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Diana":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Dr. Mundo":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Draven":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Ekko":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Elise":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Evelynn":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Ezreal":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Fiddlesticks":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Fiora":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Fizz":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Galio":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Gangplank":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Garen":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Gnar":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Gragas":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Graves":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Hecarim":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Heimerdinger":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Illaoi":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Irelia":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Ivern":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Janna":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Jarvan IV":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Jax":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Jayce":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Jhin":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Jinx":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kai'Sa":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kalista":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Karma":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Karthus":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kassadin":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Katarina":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kayle":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kayn":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kennen":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kha'Zix":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kindred":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kled":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Kog'Maw":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"LeBlanc":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Lee Sin":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Leona":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Lissandra":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Lucian":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Lulu":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Lux":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Malphite":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Malzahar":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Maokai":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Master Yi":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Miss Fortune":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Mordekaiser":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Morgana":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Nami":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Nasus":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Nautilus":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Nidalee":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Nocturne":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Nunu & Willump":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Olaf":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Orianna":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Ornn":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Pantheon":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Poppy":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Pyke":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Quinn":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Rakan":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Rammus":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Rek'Sai":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Renekton":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Rengar":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Riven":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Rumble":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Ryze":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Sejuani":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Shaco":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Shen":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Shyvana":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Singed":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Sion":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Sivir":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Skarner":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Sona":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Soraka":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Swain":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Syndra":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Tahm Kench":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Taliyah":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Talon":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Taric":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Teemo":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Thresh":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Tristana":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Trundle":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Tryndamere":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Twisted Fate":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Twitch":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Udyr":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Urgot":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Varus":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Vayne":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Veigar":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Vel'Koz":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Vi":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Viktor":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Vladimir":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Volibear":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Warwick":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Wukong":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Xerath":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Xin Zhao":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Yasuo":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Yorick":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Zac":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Zed":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Ziggs":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Zilean":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Zoe":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
	"Zyra":
		{"HP":0, "HP_Plus":0, "HP5":0, "HP5_Plus":0, "MP":0, "MP_Plus":0, "MP5":0, "MP5_Plus":0, "Armor":0, "Armor_Plus":0, "MR":0, "MR_Plus":0,
		"Move_Speed":0, "Life_Steal":0, "Lethality":0, "Armor_Pen":0, "Magic_Pen":0, "Crit_Chance":0, "AS":0, "AS_Plus":0, "AD":0, "AD_Plus":0, "AP":0, "AP_Plus":0,
		"CDR":0, "En":0, "EnP5":0},
}

items = {
	"":{},
}
