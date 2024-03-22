import os


obj_dir = 'D:/Github/feifei/FlyffVS2019/Client/Model/'
src_dir = 'D:/Github/feifei/Graphics/'
filter_o3d = '.o3d'
filter_sfx = '.sfx'
cfg = ["RustiaGate02",
    "RustiaLeaf03",
    "RustiaLeaf02",
    "RustiaLeaf01",
    "RustiaBossZone03",
    "RustiaBossZone02",
    "RustiaBossZone01",
    "RustiaBossGate01",
    "RustiaBox02",
    "RustiaWoodpot01",
    "RustiaFirewood02",
    "RustiaPot01",
    "RustiaSpear01",
    "RustiaShield01",
    "Rustiafence01",
    "Rustiaflag01",
    "RustiaFirewood01",
    "RustiaBox01",
    "RustiaChair01",
    "RustiaHut03",
    "RustiaHut02",
    "RustiaHut01",
    "RustiaLusikaGate01",
    "RustiaHallwater01",
    "RustiaGate01",
    "RustiaTreasureBox01",
    "RustiaStone01",
    "RustiaTree06",
    "RustiaTree05",
    "RustiaTree04",
    "RustiaTree03",
    "RustiaTree02",
    "RustiaTree01",
    "EveXmasTree2",
    "EveXmasTree1",
    "DreadProp16",
    "DreadProp15",
    "DreadProp14",
    "DreadProp13",
    "DreadProp12",
    "DreadProp11",
    "DreadProp10",
    "DreadProp09",
    "DreadProp08",
    "DreadProp07",
    "DreadProp06",
    "DreadProp05",
    "DreadProp04",
    "DreadProp03",
    "DreadProp02",
    "DreadProp01",
    "Dreadquartz03",
    "Dreadquartz02",
    "Dreadquartz01",
    "DreadCeiling01",
    "DreadRock06",
    "DreadRock05",
    "DreadRock04",
    "DreadRock03",
    "DreadRock02",
    "DreadRock01",
    "HalloZeolite01",
    "HalloPumpkin01",
    "HalloBone01",
    "EstProp21",
    "EstProp20",
    "EstProp19",
    "EstProp18",
    "EstProp17",
    "EstProp16",
    "EstProp15",
    "EstProp14",
    "EstProp13",
    "EstProp12",
    "EstProp11",
    "EstProp10",
    "EstProp09",
    "EstProp08",
    "EstProp07",
    "EstProp06",
    "EstProp05",
    "EstProp04",
    "EstProp03",
    "EstProp02",
    "EstProp01",
    "EstPlant02",
    "EstPlant01",
    "EstTree01",
    "EstRock04",
    "EstRock03",
    "EstRock02",
    "EstRock01",
    "EstCamp11",
    "EstCamp10",
    "EstCamp09",
    "EstCamp08",
    "EstCamp07",
    "EstCamp06",
    "EstCamp05",
    "EstCamp04",
    "Quiz_Prop11",
    "Quiz_Prop10",
    "Quiz_Prop09",
    "Quiz_Prop08",
    "Quiz_Prop07",
    "Quiz_Prop06",
    "Quiz_Prop05",
    "Quiz_Prop04",
    "Quiz_Prop02",
    "Quiz_Prop01",
    "Quiz_Prop03",
      "Ominous_boRo_02",
      "Ominous_boRo_03",
      "Ominous_boRo_01",
      "Ominous_room_04",
      "Ominous_room_02",
      "Ominous_start_03",
      "Ominous_start_02",
      "Ominous_start_01",
      "ceiling_02",
      "ceiling_01",
      "Dunstatue_03",
      "Dunstatue_04",
      "Dunstatue_01",
      "Dunstatue_02",
       "DunWall10",
      "DunWall08",
      "DunWall07",
      "DunWall06",
      "DunWall05",
      "DunWall04",
      "DunWall03",
      "DunWall02",
      "DunWall01",
      "DunWall09",
      "Dunprop17",
      "Dunprop16",
      "Dunprop15",
      "Dunprop14",
      "DunProp04",
      "DunProp03",
      "DunProp02",
      "Dunprop12",
      "Dunprop11",
      "DunProp05",
      "DunProp06",
      "Dunprop07",
      "DunProp09",
      "DunProp10",
      "DunProp13",
      "DunFrame06",
      "DunFrame05",
      "DunFrame04",
      "DunFrame03",
      "DunFrame02",
      "DunFrame01",
      "DunFlag05",
      "DunFlag04",
      "DunFlag03",
      "DunFlag02",
      "DunFlag01",
      "Dundoor06",
      "Dundoor05",
      "Dundoor04",
      "Dundoor03",
      "Dundoor02",
      "Dundoor01",
      "DunColumnup",
      "DunColumn03",
      "DunColumn02",
      "DunColumn01",
      "HarPlant04",
      "HarRock03",
      "HarRock02",
      "HarRock01",
      "HarTree08",
      "HarTree05",
      "HarTree04",
      "HarTree03",
      "HarTree06",
      "HarTree02",
      "HarTree01",
      "HarTree07",
      "HarProp04",
      "HarProp03",
      "HarProp02",
      "HarProp01",
      "HarPlant16",
      "HarPlant15",
      "HarPlant14",
      "HarPlant13",
      "HarPlant12",
      "HarPlant11",
      "HarPlant10",
      "HarPlant09",
      "HarPlant08",
      "HarPlant07",
      "HarPlant06",
      "HarPlant05",
      "HarPlant03",
      "HarPlant02",
      "HarPlant01",
      "HarRuin07-01",
      "HarRuin06-02",
      "HarRuin06-01",
      "HarRuin06",
      "HarRuin05-02",
      "HarRuin05-01",
      "HarRuin05",
      "HarRuin04-03",
      "HarRuin04-02",
      "HarRuin04-01",
      "HarRuin04",
      "HarRuin03-04",
      "HarRuin03-03",
      "HarRuin03-02",
      "HarRuin03-01",
      "HarRuin03",
      "HarRuin02-02",
      "HarRuin02-01",
      "HarRuin02",
      "HarRuin01-04",
      "HarRuin01-03",
      "HarRuin01-02",
      "HarRuin01-01",
      "HarRuin01",
      "HarCamp11",
      "HarCamp10",
      "HarCamp09",
      "HarCamp08",
      "HarCamp07",
      "HarCamp06",
      "HarCamp05",
      "HarCamp04",
      "HarCamp03",
      "HarCamp02",
      "HarCamp01",
    "MiniWall02",
    "MiniWall01",
    "MiniWindow01",
    "CislandWreck04",
      "CislandWreck03",
      "CislandWreck02",
      "CislandWreck01",
      "CislandCabin05",
      "CislandCabin04",
      "CislandCabin03",
      "CislandCabin02",
      "CislandCabin01",
      "CislandTree02",
      "CislandTree01",
      "CislandStarfish05",
      "CislandStarfish02",
      "CislandStarfish01",
      "CislandShfish10",
      "CislandShfish08",
      "CislandShfish07",
      "CislandShfish06",
      "CislandShfish05",
      "CislandShfish04",
      "CislandShfish03",
      "CislandShfish02",
      "CislandShfish01",
      "CislandCoral19",
      "CislandCoral18",
      "CislandCoral17",
      "CislandCoral12",
      "CislandCoral11",
      "CislandCoral06",
      "CislandCoral05",
      "CislandCoral04",
      "CislandCoral03",
      "CislandCoral02",
      "CislandCoral01",
      "HeavenArch39",
      "Heavengate03",
      "HeavenWall37",
      "HeavenWall36",
      "HeavenWall35",
      "HeavenWall34",
      "HeavenWall33",
      "HeavenWall32",
      "HeavenWall31",
      "HeavenWall30",
      "HeavenWall29",
      "HeavenWall28",
      "HeavenWall27",
      "HeavenWall26",
      "HeavenWall25",
      "HeavenWall24",
      "HeavenWall23",
      "HeavenWall22",
      "HeavenWall21",
      "HeavenWall20",
      "HeavenWall19",
      "HeavenWall18",
      "HeavenWall17",
      "HeavenWall16",
      "HeavenWall15",
      "HeavenTorch09",
      "HeavenStatue05",
      "HeavenArch05",
      "HeavenColumn41",
      "HeavenWall38",
      "HeavenWall14",
      "HeavenWall13",
      "HeavenWall12",
      "HeavenWall11",
      "HeavenStatue04",
      "HeavenWall07",
      "HeavenWall06",
      "HeavenTorch07",
      "HeavenStatue03",
      "Heavengate02",
      "HeavenColumn40",
      "HeavenWall10",
      "HeavenWall05",
      "HeavenWall04",
      "HeavenWall03",
      "HeavenTorch06",
      "HeavenStatue02",
      "HeavenStatue01",
      "HeavenTorch041",
      "HeavenTorch08",
      "HeavenTorch05",
      "HeavenTorch04",
      "HeavenFloor03",
      "HeavenFloor02",
      "HeavenFloor01",
      "HeavenColumn11",
      "HeavenColumn10",
      "HeavenColumn09",
      "HeavenArch04",
      "HeavenArch03",
      "HeavenArch02",
      "HeavenWall09",
      "HeavenWall08",
      "HeavenWall02",
      "HeavenWall01",
      "HeavenTorch03",
      "HeavenTorch02",
      "HeavenTorch01",
      "HeavenGate01",
      "HeavenColumn08",
      "HeavenColumn07",
      "HeavenColumn06",
      "HeavenColumn05",
      "HeavenColumn04",
      "HeavenColumn03",
      "HeavenColumn02",
      "HeavenColumn01",
      "HeavenArch01",
    "DuIbPrwall03",
    "ArenaGround",
    "ArenaSculpture01",
    "GuildCombatGround",
    "Azriaice01",
    "Azriaice02",
    "Azriaice03",
    "AzriaClock02",
    "AzriaClock01",
    "AzriaThicket04",
    "AzriaThicket03",
    "AzriaThicket02",
    "AzriaThicket01",
    "AzriaFlower08",
    "AzriaFlower07",
    "AzriaFlower06",
    "AzriaFlower05",
    "AzriaFlower04",
    "AzriaFlower03",
    "AzriaFlower02",
    "AzriaFlower01",
    "AzriaTree09",
    "AzriaTree08",
    "AzriaTree07",
    "AzriaTree06",
    "AzriaTree05",
    "AzriaTree05m",
    "AzriaTree04",
    "AzriaTree03m",
    "AzriaTree03",
    "AzriaTree02m",
    "AzriaTree02",
    "AzriaTree01m",
    "AzriaTree01",
    "AzriaStone08",
    "AzriaStone07",
    "AzriaStone06",
    "AzriaStone05",
    "AzriaStone04",
    "AzriaStone03",
    "AzriaStone02",
    "AzriaStone01",
    "AzriaBridge",
    "volcane_mt_peak",
    "volcane_bush",
    "volcane_pillar02",
    "volcane_pillar01",
    "volcane_zelkova tree",
    "volcane_cave03",
    "volcane_cave02",
    "volcane_cave",
    "volcane_tree",
    "volcane_rock",
    "volcane_rock01",
    "volcane_bridge",
    "volcane_stone01_05",
    "volcane_stone01_06",
    "volcane_mt_little01",
    "volcane_mt_little",
    "volcane_stone01_04",
    "DuIbPrGr04",
    "DuIbPrGr03",
    "DuIbPrGr02",
    "DuIbPrGr01",
    "DuIbPrGr06",
    "DuIbPrGr05",
    "DuIbPrMarseCeiling",
    "DuIbPrRootProp01",
    "DuIbPrPrup01",
    "DuIbPrBrokenBlock01",
    "DuIbPrFourProp01",
    "DuIbPrTwoProp01",
    "DuIbPrBrokenProp01",
    "DuIbPrBlock01",
    "DuIbPr01",
    "DuIbPrPrJoint01",
    "DuIbPrCeiling01",
    "DuIbPrRo12",
    "DuIbPrStone",
    "DuIbPrwall01",
    "DuIbPrwall02",
    "DuIbPrMiddleProp01",
    "DuIbCoPrPlant01",
    "DuIbCoPrPlant01-1",
    "DuIbCoPrPlant01-2",
    "DuIbPrHeadbone",
    "DuIbPrRipbone01",
    "DuIbPrRo13",
    "DuIbPrTailbone",
    "DuIbPrBranch",
    "DuIbPrDoor",
    "DuIbPrAmmo",
    "DuIbPrRipbone02",
    "DuIbPrSta02",
    "DuIbPrPoll",
    "DuIbPrSta01",
    "DuDkCoPrTreewall04",
      "DuDkCoPrTreewall05",
      "DuDkCoPrTreewall03",
      "DuDkCoPrTreewall02",
      "DuDkCoPrTreewall01",
      "DuDkCoPrPlant02",
      "DuDkCoPrPlant01",
      "DuDkPrWharf03",
      "DuDkTrPrWharf01",
      "DuDkRoPrWharf02",
      "DuDkRoPrFootHold",
      "DuDkCoPrFirePot02",
      "DuDkCoPrFirePot01",
      "DuDkRoPrPrison04",
      "DuDkRoPrPrison03",
      "DuDkRoPrPrison02",
      "DuDkRoPrPrison01",
      "DuDkRoPrHall",
      "DuDkCoPrTunnelColl-04",
      "DuDkCoPrTunnelColl-03",
      "DuDkCoPrTunnelColl-02",
      "DuDkCoPrTunnelColl-01",
      "DuDkCoPrTunnel01-6",
      "DuDkCoPrTunnel01-4",
      "DuDkCoPrTunnel01-8",
      "DuDkCoPrTunnel01-2",
      "DuDkCoPrTunnel01-7",
      "DuDkCoPrTunnel01-5",
      "DuDkCoPrTunnel01-9",
      "DuDkCoPrTunnel01-3",
      "DuDkCoPrTunnel01-1",
      "DuDkRoPrironGa01",
      "DuDkTrPrGate01",
      "DuDkTrPrGateT01",
      "DuDkKiStoneGateT",
      "DuDkKiStoneGate",
      "DuDkCoPrRock04",
      "DuDkCoPrRock03",
      "DuDkCoPrRock02",
      "DuDkCoPrRock01",
      "DuDkRoPrGrEgg09",
      "DuDkRoRrGrEgg10",
      "DuDkTrPrEgg03",
      "DuDkTrPrEgg03",
      "DuDkTrPrEgg03",
      "DuDkTrPrEgg02",
      "DuDkTrPrEgg01",
      "DuDkRoPrEgg01",
      "DuDkRoRrGrEgg08",
      "DuDkRoRrGrEgg07",
      "DuDkRoRrGrEgg06",
      "DuDkRoRrGrEgg05",
      "DuDkRoRrGrEgg04",
      "DuDkRoRrGrEgg03",
      "DuDkRoRrGrEgg02",
      "DuDkRoRrGrEgg01",
      "DuDkKiPro02",
      "DuDkKiPro01",
      "DuDkKitent01",
      "DuDkCoPrChimney01-01",
    "DuDkCoPrFirewood",
    "DuDkCoPrStone01",
    "DuDkCoPrDaPrSignalLamp",
      "DuDkCoPrCr03",
      "DuDkCoPrCr02",
      "DuDkCoPrCr01",
      "DuDkCoPrBox01_03",
      "DuDkCoPrBox01_02",
      "DuDkCoPrBox01_01",
      "DuDkCoPrMineLight02",
      "DuDkCoPrMineLight01",
      "DuDkCoPrMine06",
      "DuDkCoPrMine05",
      "DuDkCoPrMine03",
      "DuDkCoPrMine04",
      "DuDkCoPrMine02",
      "DuDkCoPrMine01",
      "DuDkCoPrRail180",
      "DuDkCoPrRail90R",
      "DuDkCoPrRail90L",
      "DuDkCoPrRail45R",
      "DuDkCoPrRail45L",
      "DuDkCoPrRail45",
      "MaflPrMarseEnter",
      "MaFlPrMarseMu04",
      "MaFlPrMarseMu03",
      "MaFlPrMarseMu02",
      "MaFlPrMarseMu01",
      "MaFlPrMarseFirePillar",
      "MaFlPrMarseToWheel",
      "MaFlPrMaTotemFStone",
      "MaFlPrMaTotemStone",
      "MaFlPrMarseRuTotem02",
      "MaFlPrMarseRuTotem01",
      "MaFlPrMarseTotem03",
      "MaFlPrMarseTotem02",
      "MaFlPrMarseTotem01",
    "MaFlPrMarseRuFountian",
    "MaFlPrMarseFountian",
    "MaflPrMarseRoot04",
    "MaflPrMarseRoot03",
    "MaflPrMarseRoot02",
    "MaflPrMarseRoot01",
    "MaFlPrGrGe02",
    "MaFlPrGrGe01",
    "MaFlPrMarseMarStone01",
    "MaFlPrMarseMarStone02",
    "MaFlPrMarseMarStone03",
    "MaFlPrMarseMarStone04",
    "MaFlPrMarseTorch01",
    "MaFlPrMarseTorch",
      "MaFlPrMarseString",
      "MaFlPrMarseCeiling01",
      "MaFlPrMarseCeiling",
      "MaFlPrMarseVine02",
      "MaFlPrMarseVine01",
      "MaFlPrMarse_Pilar01",
      "MaFlPrMarse_Pilar",
      "MaFlPrMarseStoneGateT",
      "MaFlPrMarseStoneGate",
      "MaFlPrMarsefountain02",
      "MaFlPrMarseItemBox-02",
      "MaFlPrMarseItemBox-01",
      "MaFlPrMarseLever",
      "MaFlPrMarsefountain",
      "MaMaPrBridge-01",
    "MaMaPrSide",
    "MaMaPrRock04",
    "MaMaPrRock03",
    "MaMaPrRock02",
    "MaMaPrRock01",
    "MaMaPrStone",
    "MaMaPrP03",
    "MaMaPrP02",
    "MaMaPrP01",
    "MaMaPrBox_B04",
      "MaMaPrBox_B03",
      "MaMaPrBox_B02",
      "MaMaPrBox_B01",
    "mamaprwindow",
    "MaMaPrTree",
    "MaMaPrTailbone",
    "MaMaPrPyramid03-01",
    "MaMaPrRipbone02",
    "MaMaPrRipbone01",
    "MaMaPrHeadbone",
    "MaMaPrAmmo01",
    "MaMaPrAmmo",
    "MaMaPrPyramid02",
    "MaMaPrPyramid01",
    "MaMaPrBridge02",
    "MaMaPrBridge01",
    "MaMaPrBox04",
    "MaMaPrBox03",
    "MaMaPrBox02",
    "MaMaPrBox01",
    "MaTaPrRock04",
    "MaTaPrRock03",
    "MaTaPrRock02",
    "MaTaPrRock01",
    "MaTaPrBvidge02",
    "MaTaPrBvidge01",
    "MaTaPrPillar",
    "MaTaPrPillar-Up",
    "MaTaPrPillar-G",
    "MaTaPrPillar-Down",
    "MaTaPrBigDoor-01C",
    "MaTaPrVine-Area",
    "MaTaPrVine-Vine",
    "MaTaPrVine-bg",
    "MaTaPrBrackenPlant",
    "MaTaPrBracken",
    "MaTaPrLongGrass",
    "MaTaPrBranch-02",
    "MaTaPrBranch-01",
    "MaTaPrBranch",
    "MaTaPrLeaves",
    "RainbowStart02",
    "RainbowStart01",
    "MaDaPrFence",
    "MaEveHalloween",
    "EveXmasTree",
    "MaMaPrDome04",
    "MaMaPrDome03",
    "MaMaPrDome02",
    "MaMaPrDome01",
    "MaSuPrBigDoorTC",
    "MaSuPrBigDoorC",
    "MaSuFaDome01",
    "MaSuFaDome02",
    "MaSuFaDome03",
    "MaSuFaDome04",
    "MaSuFaDomeCenter",
    "MaSuFaDomeleg",
    "MaSuPrWarp",
    "MaSuPrGateway",
    "MaSuPrGateway01",
    "MaSuPrGateway02",
    "MaSuPrCaveLongRed",
    "MaSuPrCaveRed",
    "pkdudkroprwharf02",
    "wharf",
    "magiczone",
      "thunder03",
      "thunder02",
      "thunder01",
    "tree01",
      "firem02",
      "firem01",
      "fire03",
      "fire02",
      "fire01",
      "firem",
      "bu01",
      "riverred01",
      "rivergreen01",
      "illumination01",
    "madaarmory",
      "skylight01",
      "skylight03",
      "skylight",
      "clouds04",
      "clouds03",
      "clouds02",
      "clouds01",
      "glowfly05",
      "glowfly04",
      "glowfly03",
      "glowfly02",
      "glowfly01",
      "glowfly",
    "madalodestar",
    "magiclight",
    "enterdungeon",
    "MaCoPrSkySign05",
    "MaCoPrSkySign04",
    "MaCoPrSkySign03",
    "MaCoPrSkySign02",
    "MaCoPrSkySign01",
    "MaDaPrCogwheelM-D",
    "MaDaPrCogwheelM",
    "MaDaPrLongM04",
    "MaDaPrLongM03",
    "MaDaPrLongM02",
    "MaDaPrLongM01",
    "MaDaStation",
    "MaDaPrWaterLight",
    "MaDaLodeStar",
    "MaDaPrHeapC",
    "MaFIPrSi03C",
    "MaDaPrChimney01C",
    "MaDaPrSignalLampC",
    "MaDaPrWagonSmall02C",
    "MaDaPrWagonSmall01C",
    "MaDaPrBar03C",
    "MaDaPrBar02C",
    "MaDaPrBar01C",
    "MaDaPrConveyor02C",
    "MaDaPrConveyor01C",
    "MaDaPrWagonBigC",
    "MaDaPrCraneSmallC",
    "MaDaPrDigMachine01c",
    "MaDaPrStairC",
    "MaDaPrSupport01C",
      "MaDaPrStoneBvidge02",
      "MaDaPrStoneBvidge01",
      "MaDaPrLightMushroomB02",
      "MaDaPrLightMushroomB01",
      "MaDaPrLightMushroom03",
      "MaDaPrLightMushroom02",
      "MaDaPrLightMushroom01",
      "MaDaGeneralStore01",
      "MaDaRestaurant",
      "MaDaMagicShop",
      "MadaArmory",
      "MaDaCoOffice",
      "MaDaPipeTopC901",
      "MaDaPipeTop4502",
      "MaDaPipeTopC4501",
      "MaDaPipeSideS",
      "MaDaPipeSideLongC90",
      "MaDaPipeSideLongC18002",
      "MaDaPipeSideLongC18001",
      "MaDaPipeSideJointC05",
      "MaDaPipeSideJointC04",
      "MaDaPipeSideJointC02",
      "MaDaPipeSideJointC01",
      "MaDaPipeSideC9002",
      "MaDaPipeSideC9001",
      "MaDaPipeSideC4503",
      "MaDaPipeSideC4502",
      "MaDaPipeSideC02",
      "MaDaPipeSideC01",
      "MaDaPrCogwheelM",
      "MaCoPrGrGe05",
      "MaCoPrGrGe05_1",
      "MaCoPrGrGe01C-04",
      "MaCoPrGrGe01C-03",
      "MaCoPrGrGe01C-02",
      "MaCoPrGrGe01C-01",
      "MaDaGeneralStore02",
      "madafrsteelshotC",
      "madafrsteellongC",
      "madafrsteelgroupC",
      "MaDaPrStorage03C",
      "MaDaPrStorage02C",
      "MaDaPrStorage01C",
      "MaDaPrReC90L",
      "MaDaPrReC90R",
      "MaDaPrReC45R",
      "MaDaPrReC45L",
      "MaDaPrReC1802",
      "MaDaPrReC1801",
      "MaDaPrFan0103C",
      "MaDaPrFan0102C",
      "MaDaPrFan0101C",
      "MaDaPrFan0203C",
      "MaDaPrFan0202C",
      "MaDaPrFan0201C",
      "MaDaPrDrum02",
      "MaDaPrDrum01",
      "MaCoPrDr07C",
      "MaCoPrDr06C",
      "MaCoPrDr05C",
      "MaCoPrDr04C",
      "MaCoPrDr03C",
      "MaCoPrDr02C",
      "MaCoPrDr01C",
      "MaDaPrMiddleBox01C",
      "MaDaPrBigBox01C",
      "MaDaPrConBox02C",
      "MaDaPrConBox01C",
      "MaDaPrCliff09C",
      "MaDaPrCliff08C",
      "MaDaPrCliff07C",
      "MaDaPrCliff06C",
      "MaDaPrCliff05C",
      "MaDaPrCliff04C",
      "MaDaPrCliff03C",
      "MaDaPrCliff02C",
      "MaDaPrCliff01C",
      "MaDaPrLightSmallC",
      "MaDaPrGroundWindow01C",
      "MaDaPrLightBigC",
      "MaSaPrStLi01C",
      "MaDaPrRail90RC",
      "MaDaPrRail90LC",
      "MaDaPrRail45RC",
      "MaDaPrRail45LC",
      "MaDaPrRail45C",
      "MaDaPrRail180C",
      "MaDaPrSupportC",
      "MaDaPrRevTreeC",
      "MaDaPrRevetmentC90R",
      "MaDaPrRevetmentC90L",
      "MaDaPrRevetmentC45R",
      "MaDaPrRevetmentC45L",
      "MaDaPrRevetmentC1802",
      "MaDaPrRevetmentC1801",
      "MaDaPrRevetmentC01",
      "MaDaPrLightRock04",
      "MaDaPrLightRock03",
      "MaDaPrLightRock02",
      "MaDaPrLightRock01",
      "MaDaPrCaveLong_C",
      "MaDaPrCaveLong_B02",
      "MaDaPrCaveLong_B01",
      "MaDaPrCaveLong_A02",
      "MaDaPrCaveLong_A01",
      "MaDaPrCaveDown_C02",
      "MaDaPrCaveDown_C01",
      "MaDaPrCave_C",
      "MaDaPrCave_B_a",
      "MaDaPrCave_B",
      "MaDaPrCave_A_aa",
      "MaDaPrCave_A_a",
      "MaDaPrCave_A",
      "MaDaPrCave_A",
      "MaSaPrRo0901C",
      "MaSaPrRo09C",
      "MaSaPrRo0301C",
      "MaSaPrRo02C",
      "MaSaPrRo038C",
      "MaSaPrRo037C",
      "MaSaPrRo028C",
      "MaSaPrRo27C",
      "MaCoPrRo13C",
      "MaCoPrRo12C",
      "MaCoPrRo11C",
      "MaCoPrRo10C",
      "MaCoPrBo01C",
      "MaFlPrPack03C",
      "MaCoPrBo01C-02",
      "MaCoPrBo01C-01",
      "MaDaPrMineTree02",
      "MaDaPrMineTree01",
      "MaDaPrMine06",
      "MaDaPrMine055",
      "MaDaPrMine05",
      "MaDaPrMine044",
      "MaDaPrMine04",
      "MaDaPrMine03",
      "MaDaPrMine01",
      "MaDaReq01-01",
      "MaDaReq01",
      "madafrsteelshot",
      "madafrsteellong",
      "madafrsteelgroup_03",
      "madafrsteelgroup_02",
      "madafrsteelgroup_01",
      "MaDaPrRevetmentset01",
      "MaDaPrRoad45L",
      "MaDaPrRoad45R",
      "MaDaPrRoad90L",
      "MaDaPrRoad90R",
      "MaDaPrRoad90L01",
      "MaDaPrRoad1802",
      "MaDaPrRoad1801",
      "MaDaPrCliff09",
      "MaDaPrCliff08",
      "MaDaPrCliff07",
      "MaDaPrCliff06",
      "MaDaPrCliff05",
      "MaDaPrCliff04",
      "MaDaPrCliff03",
      "MaDaPrCliff02",
      "MaDaPrCliff01",
      "MaDaPipeTop90",
      "MaDaPipeSideLong90",
      "MaDaPipeSideS",
      "MaDaPipeSideLong18002",
      "MaDaPipeSideLong18001",
      "MaDaPipeTop4502",
      "MaDaPipeTop4501",
      "MaDaPipeSideLong4502",
      "MaDaPipeSideLong4501",
      "MaDaPipeSideJoint05",
      "MaDaPipeSideJoint04",
      "MaDaPipeSideJoint03",
      "MaDaPipeSideJoint02",
      "MaDaPipeSideJoint01",
      "MaDaPipeSide9002",
      "MaDaPipeSide9001",
      "MaDaPipeSide4504",
      "MaDaPipeSide4503",
      "MaDaPipeSide4502",
      "MaDaPipeSide4501",
      "MaDaPipeSide02",
      "MaDaPipeSide01",
      "MaDaPrTree07",
      "MaDaPrTree06",
      "MaDaPrTree05",
      "MaDaPrTree04",
      "MaDaPrTree03",
      "MaDaPrTree02",
      "MaDaPrTree01",
      "MaDaPrHeap",
      "MaDaPrFan0103",
      "MaDaPrFan0102",
      "MaDaPrFan0101",
      "MaDaPrFan0201",
      "MaDaPrFan0202",
      "MaDaPrFan0203",
      "MaDaPrRevetmentIron1802",
      "MaDaPrRevetmentIron1801",
      "MaDaPrRevetmentIron90R",
      "MaDaPrRevetmentIron90L",
      "MaDaPrRevetmentIron45R",
      "MaDaPrRevetmentIron45L",
    "MaDaPrBar01",
    "MaDaPrBar02",
    "MaDaPrBar03",
    "MaDaPrBigBox01",
    "MaDaPrChimney01",
    "MaDaPrConBox02",
    "MaDaPrConveyor01",
    "MaDaPrConveyor02",
    "MaDaPrCraneSmall",
    "MaDaPrDigMachine01",
    "MaDaPrGroundWindow01",
    "MaDaPrLightBig",
    "MaDaPrLightSmall",
    "MaDaPrMiddleBox01",
    "MaDaPrPump01",
    "MaDaPrRail180",
    "MaDaPrRail45",
    "MaDaPrRail45L",
    "MaDaPrRail45R",
    "MaDaPrRail90L",
    "MaDaPrRail90R",
    "MaDaPrRevetment1801",
    "MaDaPrRevetment1802",
    "MaDaPrRevetment45R",
    "MaDaPrRevetment45L",
    "MaDaPrRevetment90L",
    "MaDaPrRevetment90R",
    "MaDaPrRevSupport",
    "MaDaPrRevTree",
    "MaDaPrSignalLamp",
    "MaDaPrStair",
    "MaDaPrStorage01",
    "MaDaPrStorage02",
    "MaDaPrStorage03",
    "MaDaPrSupport01",
    "MaDaPrWagonBig",
    "MaDaPrWagonSmall01",
    "MaDaPrWagonSmall02",
    "MaSaPuHead03",
    "MaSaPuFence02",
    "MaSaPuHouse03",
    "MaSaPuHouse02",
    "MaSaPuHouse01",
    "MaPrPumpstem01",
    "MaSaPuFence01",
    "MaSaPuScarecrow01",
    "MaSaPuHead",
    "MaSaPuHead02",
    "MaSaPuHead04",
    "MaSaPumkinPole01",
    "dunTest",
    "MaPrSmCr02",
    "MaPrSmCr01",
    "MaCoPrGrGe01-01",
    "MaCoPrGrGe01-02",
    "MaCoPrGrGe01-03",
    "MaCoPrGrGe01-04",
    "MaFlPrFlis01",
    "MaCoPrViaduct01-1",
    "MaCoPrLoLl01-2",
    "MaCoPrLoLl01-1",
      "MaCoPrGr5",
      "MaCoPrGr4",
      "MaCoPrGr3",
    "MaCoPrViaduct01",
    "MaCoPrLoLl01",
      "MaCoPrDr02",
      "MaCoPrDr01",
      "MaCoPrDr07",
      "MaCoPrDr06",
      "MaCoPrDr05",
      "MaCoPrDr04",
      "MaCoPrDr03",
      "MaCoPrRo13",
      "MaCoPrRo12",
      "MaCoPrRo04",
      "MaCoPrRo11",
      "MaCoPrRo10",
      "MaCoPrBa01",
      "MaCoPrOi",
      "MaCoPrRi01",
      "MaCoPrSi05",
      "MaCoPrSi04",
      "MaFlPrPack03",
      "MaCoPrBo01-02",
      "MaCoPrBo01-01",
      "MaCoPrBo01",
      "MaCoPrFl03-02",
      "MaCoPrFl02-04",
      "MaCoPrFl02-03",
      "MaCoPrFl02-02",
      "MaCoPrFl02-01",
      "MaCoPrFl03-04",
      "MaCoPrFl03-03",
      "MaCoPrFl03-01",
      "MaCoPrTr20",
      "MaCoPrTr15",
      "MaCoPrTr14",
      "MaCoPrTr13",
      "MaCoPrTr11",
      "MaCoPrTr10",
      "MaFlPrTr04",
      "MaCoPrTr02",
      "MaCoPrTr01",
      "MaFlPrTr05",
      "MaCoPrTr05",
      "MaCoPrTr04",
      "MaPrSt001",
      "MaCoPrTr03",
      "MaCoPrTr12",
      "MaCoPrMu03",
      "MaCoPrMu04",
      "MaPrMu001",
      "MaCoPrMu05",
      "MaCoPrMu06",
      "MaPrMu002",
      "MaCoPrGr01",
      "MaCoPrGr2",
      "MaCoPrGr04",
      "MaCoPrGr1",
      "MaCoPrGr05",
      "MaCoPrGr06",
      "MaCoPrGr07-04",
      "MaCoPrGr07-03",
      "MaCoPrGr07-02",
      "MaCoPrGr07",
    "MaCoPrRo06",
    "MaSaLs01-2",
    "MaSaLs01-1",
      "MaRiPrFourProp03",
      "MaRiPrRootProp02",
      "MaRiPrRootProp01",
      "MaRiPrFourProp02",
      "MaRiPrPrup02",
      "MaRiPrPrup03",
      "MaRiPrBrokenBlock01",
      "MaRiPrBrokenBlock02",
      "MaRiPrFourProp01",
      "MaRiPrPrup01",
      "MaRiPr10",
      "MaRiPrTwoProp02",
      "MaRiPrBrokenProp01",
      "MaRiPrBrokenProp02",
      "MaRiPrBlock01",
      "MaRiPrBlock02",
      "MaRiPrTwoProp01",
      "MaRiPr11",
      "MaRiPrPrJoint02",
      "MaRiPrMiddleProp01",
      "MaRiPrMiddleProp02",
      "MaRiPrCeiling01",
      "MaRiPrCeiling02",
      "MaRiPrPrJoint01",
      "aaaa",
      "MaSaFightingGround",
      "MaSaprFlowerBed",
      "MaSaReq01",
      "MaSaReq01-01",
      "MaSaHo26",
      "MaSaHo21",
      "MaSaHo22",
      "MaSaHo23",
      "MaSaHo24",
      "MaSaHo25",
      "MaSaHo16",
      "MaSaHo11",
      "MaSaHo12",
      "MaSaHo13",
      "MaSaHo14",
      "MaSaHo15",
      "MaSaPrThTr01",
      "MaSaPrSupport01",
      "MaSaprBench01",
      "MaSaLs01",
      "MaSaPrFlag03",
      "MaSaPrFlag04",
      "MaSaPrFlag05",
      "MaSaPrBridge01",
      "MaSaPrFlag02",
      "MaSaPrFlag01",
      "MaSaWagon01",
      "MaSaPrStLi01",
      "MaSaPrCa01",
      "MaSaPrRo02",
      "MaSaPrDoSt01",
      "MaSaPrRo09",
      "MaSaPrRo03",
      "MaSaPrDoSt01-02",
      "MaCoPrStWa04",
      "MaCoPrStWa02",
      "MaSaPrCiEn01",
      "MaCoPrStWa01",
      "MaCoPrStJo01",
      "MaCoPrStJo02",
      "MaCoPrStWa03",
      "MaSaPrWharf02",
      "MaSaPrWharf01",
      "MaSaSlope05",
      "MaSaSlope02",
      "MaSaSlope03",
      "MaSaSlope04",
      "MaSaSlope01",
        "MaSaBkRouInRi02",
        "MaSaBkRouInRi01",
        "MaSaBkRouInRi03",
        "MaSaBkRouInLe03",
        "MaSaBkRouInLe02",
        "MaSaBkRouInLe01",
        "MaSaBkRouOutLe01",
        "MaSaBkRouOutLe02",
        "MaSaBkRouOutLe03",
        "MaSaBkRouOutRi01",
        "MaSaBkRouOutRi02",
        "MaSaBkRouOutRi03",
        "MaSaBkInLe01",
        "MaSaBkInRi01",
        "MaSaBkOutRi01",
        "MaSaBkOutLe01",
        "MaSaBkDiaInLe01",
        "MaSaBkDiaInRi01",
        "MaSaBkDiaOutRi01",
        "MaSaBkDiaOutLe01",
        "MaSaBkDiagonal03",
        "MaSaBkDiagonal02",
        "MaSaBkDiagonal01",
        "MaSaBkSide01",
        "MaSaBkSide02",
        "MaSaBkSide03",
    "MaSaHo01",
    "MaSaHo02",
    "MaSaRestaurant",
    "MaSaGe01",
    "MaSaPrCr01",
    "MaSaSaHa01",
    "MaSaMagic01",
    "MaSaHo06",
    "MaSaPrLi01",
    "MaSaHo10",
    "MaSaHo04",
    "MaSaAr01",
    "MaSaHo03",
    "MaSaHo05",
    "genlodestar02Coll",
      "MaFlHala03",
      "MaFlHala02",
      "MaFlHala01",
      "MaFlHaro01",
      "MaFlHaro02",
        "MaFlPrAnvi01",
        "MaFlPrLopa01",
        "MaFlPrRack01",
        "MaFlPrBr03",
        "MaCoPrTe01",
        "MaFlPrTe01",
        "MaFlPrTe02",
        "MaFlPrFe02",
        "MaFlPrFe05",
        "MaFlPrFe04",
        "MaFlPrFe06",
        "MaFlPrFe03",
        "MaFlPrFe01",
        "MaFIPrLa02",
        "MaFlPrLa01",
        "MaFlPrSi03",
        "MaFlPrSi04",
        "MaFlPrSi05",
        "MaFlPrSi02",
        "MaFlPrSi01",
      "MaFlPrCa01",
      "MaFlPrLa03",
      "MaFlPrPo01",
      "MaFlPrPo02",
      "MaCoLl01",
      "MaFlPrBenc01",
      "MaFlReq01-01",
      "MaFlReq01",
      "MaFlRe01",
      "MaFlWi01",
      "MaKoGe03",
      "MaKoGe02",
      "MaKoGe01",
      "MaFlSt001",
      "MaFlPrGe01",
      "MaFlLs001",
      "MaFlHo01",
      "MaFlHo02",
      "MaFlFo001",
      "MaFlCi001",
      "MaFlAr01",
      "default"]

def find_file(dest_dir: str, extension:str) -> list:
    # 在对os进行调取的时候，返回三个参数
    # for循环自动完成递归枚举
    # 三个参数：分别返回
    # 1.父目录（当前路径）parent
    # 2.父目录下的所有文件夹名字 dirnames
    # 3.父目录下的所有文件名字 filenames
    files = []
    for parent,dirnames,filenames in os.walk(dest_dir):
        # 很多时候需要忽略一些特定目录
        # 忽略 "someenv" and "__pycache__" 目录中
        dirnames[:] = [d for d in dirnames if d not in ['someenv','__pycache__']]
        # 这里完成了对dirnames的筛选，也就是说在接下来的for循环中，
        # someenv和__pycache__将不会被walk
        # 然后，选中所有以".md"结尾的文件
        filenames[:] = [f for f in filenames if f.endswith(extension)]
        for filename in filenames:
            #输出找到的文件目录
            # print("the full name of the file is :",
            #     os.path.join(parent,filename))
            files.append(filename.lower())

    return files
            

o3d_files:list = find_file(obj_dir, filter_o3d)
# print(o3d_files, len(o3d_files))
# print('---')
src_o3d_files = find_file(src_dir, filter_o3d)
src_sfx_files = find_file(src_dir, filter_sfx)
print(src_o3d_files, len(src_o3d_files))

kebaras = ["MaCoPrSkySign01",
"MaTaPrVine-Area",
"MaTaPrVine-Vine",
"MaMaPrTree",
"MaCoPrGrGe01-04",
"MaCoPrGrGe01-01",
"MaTaPrBvidge02",
"MaTaPrPillar",
"MaTaPrPillar-Up",
"tree01",
"MaRiPrFourProp01",
"MaCoPrLoLl01-2",
"DuDkCoPrFirePot01",
"MaSaPrFlag05",
"fire01",
"MaMaPrBridge01",
"MaMaPrBridge02",
"MaMaPrRipbone01",
"MaMaPrBox02",
"MaMaPrRock04",
"fire03",
"clouds04",
"MaMaPrTailbone",
"MaMaPrRipbone02",
"MaMaPrHeadbone",
"MaMaPrAmmo01",
"MaMaPrAmmo",
"MaCoPrRo11",
"MaCoPrRo10",
"MaMaPrStone",
"clouds03",
"clouds01",
"MaMaPrRock03",
"MaMaPrRock02",
"MaMaPrRock01",
"firem02",
"firem01",
"MaCoPrSkySign03",
"MaCoPrGrGe05_1",
"MaCoPrGrGe01C-01",
"MaCoPrGrGe01C-02",
"MaSuPrCaveRed",
"MaCoPrTr14",
"enterdungeon",
"MaDaPrStoneBvidge01",
"MaDaPrStoneBvidge02",
"MaTaPrBranch-01",
"MaTaPrBranch",
"MaTaPrLeaves",
"clouds02",
"MaCoPrTr20",
"skylight03",
"MaCoPrTr12",
"MaCoPrSkySign04",
"MaTaPrBigDoor-01C",
"MaSuPrBigDoorC",
"MaTaPrRock03",
"MaTaPrRock02",
"MaTaPrLongGrass",
"MaTaPrBracken",
"MaTaPrRock01",
"MaSaHo23",
"MaCoPrGr4",
"MaSaprBench01",
"MaCoPrGr2",
"MaCoPrGr04",
"MaCoPrMu03",
"MaCoPrFl02-01",
"MaCoPrFl02-02",
"MaCoPrFl03-02",
"MaCoPrRo12",
"MaCoPrRo04",
"MaCoPrGrGe01-02",
"MaCoPrTr04",
"MaTaPrBvidge01",
"rivergreen01",
"MaTaPrRock04",
"glowfly01",
"glowfly04",
"glowfly03",
"MaTaPrVine-bg",
"MaDaPrCave_A_aa",
"MaSaPrRo27C",
"MaSaPrRo037C",
"MaSaPrRo028C",
"glowfly02",
"MaFlPrFlis01",
"MaMaPrBox04",
"MaMaPrBox03",
"MaMaPrP02",
"bu01",
"MaMaPrPyramid02",
"MaMaPrBox01",
"MaSuPrGateway",
"mamaprwindow",
"MaMaPrPyramid03-01",
"MaMaPrP03",
"MaMaPrPyramid01",
"MaMaPrP01",
"thunder01",
"DuDkRoPrHall",
"MaDaPipeSideLong18002",
"MaDaPipeSideC01",
"MaDaPipeSide01",
"MaDaPipeSideJoint04",
"MaDaPrLongM03",
"MaDaPipeSideJoint02",
"MaDaPipeSideJoint01",
"MaDaPipeSide9001",
"MaSuPrGateway02",
"MaDaPipeSide02",
"MaDaPrStorage03",
"MaSuFaDomeleg",
"MaSuFaDome04",
"MaSuFaDome01",
"MaSuFaDomeCenter",
"MaSuFaDome03",
"MaSuFaDome02",
"MaDaPipeSideLong18001",
"MaDaPipeSideLong4502",
"MaDaPipeSide4503",
"MaMaPrBridge-01",
"MaMaPrSide",
"MaMaPrDome04",
"MaMaPrDome03",
"MaMaPrDome02",
"MaSuPrGateway01",
"MaCoPrSkySign02",
"MaCoPrDr07",
"MaCoPrDr03",
"MaCoPrDr06",
"MaCoPrBo01",
"MaCoPrDr05",
"MaFlPrPack03",
"MaCoPrBo01-01",
"MaCoPrTr13",
"MaFlPrRack01",
"MaCoPrTe01",
"MaFlPrPo02",
"MaDaPrMineTree02",
"MaDaPrTree07",
"MaSaWagon01",
"MaSaPrCa01",
"MaSaPrRo02",
"MaFlPrPo01",
"MaDaPrMine06",
"MaDaPrRail45C",
"MaDaPrRail45RC",
"MaDaPrConveyor01C",
"MaDaPrWagonBigC",
"MaDaPrWagonSmall02C",
"MaTaPrPillar-G",
"MaTaPrPillar-Down",
"MaDaPrLightMushroomB02",
"MaDaPrLightMushroomB01",
"MaDaPrLightMushroom03",
"MaDaPrLightMushroom02",
"MaDaPrRail45LC",
"MaDaPrRail180C",
"MaDaPrRail90LC",
"MaDaPrRail90RC",
"MaDaPrConveyor02C",
"MaDaPrWagonSmall01C",
"MaDaPrBar01C",
"MaDaPrSupport01C",
"MaDaPrCaveLong_B02",
"MaDaPrLongM02",
"MaDaPrLongM01",
"MaDaPrSignalLampC",
"MaDaPrLightSmallC",
"MaDaPrLightBigC",
"MaSaPrRo038C",
"glowfly",
"fire02",
"MaDaPrFan0103",
"MaDaPrChimney01C",
"MaDaPrChimney01",
"MaFlPrLopa01",
"MaFlPrAnvi01",
"MaFlPrTe01",
"MaTaPrBrackenPlant",
"MaSaPrRo03",
"MaSaPrRo09",
"MaCoPrGr01",
"MaSuPrWarp",
"MaDaPrReC90L",
"MaDaPrReC1802",
"MaDaPrReC90R",
"MaDaPrReC1801",
"MaDaPrReC45L",
"MaDaRestaurant",
"MaDaMagicShop",
"MadaArmory",
"MaDaCoOffice",
"MaDaPrCogwheelM",
"MaDaPrWaterLight",
"MaDaPrStorage02C",
"MaCoPrGrGe05",
"MaPrSmCr01",
"MaDaPrMiddleBox01",
"MaDaPrLightSmall",
"MaDaGeneralStore01",
"MaDaPrDrum01",
"MaDaPrLightMushroom01",
"MaDaPrBar02C",
"MaDaPrCave_A_a",
"MaDaPrCaveLong_A02",
"MaDaPrMiddleBox01C",
"MaDaPrBigBox01C",
"MaDaPrFan0103C",
"MaDaPrStorage03C",
"MaDaPipeSideLongC18001",
"MaDaPipeTopC901",
"MaDaPipeSideLongC18002",
"MaDaPipeSideJointC04",
"MaDaPipeSideC9001",
"MaDaPipeTopC4501",
"MaDaPipeSideJointC01",
"MaDaPipeSideLongC90",
"MaDaPipeSideC9002",
"MaDaPipeSideS",
"MaDaPipeSideC4502",
"MaDaPipeSide9002",
"MaDaPipeSideLong90",
"MaDaPrCaveDown_C02",
"MaDaStation",
"MaDaGeneralStore02",
"MaDaLodeStar",
"magiclight",
"madalodestar",
"MaDaPrLongM04",
"illumination01",
"MaDaPrCogwheelM-D",
"MaDaPrStairC",
"MaSuPrCaveLongRed",
"riverred01",
"MaSuPrBigDoorTC",
"MaDaReq01",
"MaDaReq01-01",
"DuDkKitent01",
"DuDkCoPrDaPrSignalLamp",
"MaDaPrFence",
"pkdudkroprwharf02",
"RainbowStart01",
"RainbowStart02",
"glowfly05",
"MaFlPrFe04",
"MaFlPrFe06",
"MaFlPrFe05",
"MaFlPrFe03",
"MaFlPrFe01",
"magiczone",
"MaDaPrCaveLong_C",
"MaDaPrCave_B",
"MaDaPrCaveDown_C01",
"MaDaPrCave_A",
"madafrsteellongC",
"MaDaPrCave_B_a",
"madafrsteelgroupC",
"RustiaTree01",
"EstProp17",
"EstProp18",
"MaCoPrGr3",
"MaCoPrGr5",
"RustiaGate02",
"MaCoPrSkySign05",
"MaCoPrDr04",
"MaCoPrDr02",
"MaDaPrBar01",
"MaDaPrWagonBig",
"MaDaPrWagonSmall02",
"MaDaPrRail90R",
"MaDaPrRail180",
"MaDaPrRail45L",
"MaDaPrRail45R",
"MaDaPrMine01",
"MaDaPrConveyor01",
"MaDaPrMine044",
"MaDaPrConveyor02",
"MaDaPrMine05",
"MaDaPrSignalLamp",
"MaDaPrRail45",
"MaDaPrSupport01",
"MaDaPrWagonSmall01",
"MaDaPrRevetmentset01",
"MaDaPrConBox02",
"MaDaPrBar03",
"MaDaPrRevSupport",
"MaDaPrBigBox01",
"MaDaPrBar02",
"MaDaPrCraneSmall",
"MaDaPrHeap",
"MaDaPrMineTree01",
"MaDaPrLightBig",
"MaCoPrRo13",
"MaDaPrLightRock04",
"MaDaPrLightRock02",
"MaDaPrLightRock01",
"MaDaPrLightRock03",
"MaDaPrMine03",
"MaDaPrMine04",
"DuDkTrPrGate01",
"MaDaPrCave_C",
"MaCoPrRo10C",
"MaCoPrRo11C",
"MaDaPrRevetmentIron1802",
"MaDaPrRevetmentIron1801",
"MaDaPrRevetmentIron45L",
"MaDaPrRevetmentIron90R",
"MaDaPrRevetmentIron90L",
"MaDaPrFan0101",
"MaDaPrFan0102",
"MaDaPrRoad45L",
"MaDaPrRoad1801",
"MaDaPrRoad1802",
"MaDaPrStair",
"MaDaPrDigMachine01",
"MaDaPrStorage02",
"MaDaPrGroundWindow01",
"MaDaPrFan0201",
"MaDaPrFan0202",
"MaDaPrFan0203",
"MaDaPrRoad90L",
"MaDaPrRoad90L01",
"MaDaPrRoad45R",
"MaCoPrGrGe01-03",
"madafrsteelgroup_03",
"madafrsteelgroup_01",
"madafrsteelshot",
"MaSaHo16",
"MaSaPrFlag01",
"MaSaHo25",
"MaSaHo11",
"MaSaHo12",
"MaSaHo22",
"MaDaPrRevetment45L",
"MaDaPrRevetment1802",
"MaDaPrRevetment1801",
"MaDaPrStorage01",
"MaCoPrBo01-02",
"MaDaPrRevetment90R",
"MaCoPrDr01",
"MaCoPrRo06",
"MaDaPrRevetment90L",
"MaDaPipeSide4501",
"MaDaPipeSideJoint05",
"MaDaPipeSide4504",
"MaDaPipeTop90",
"MaDaPipeSideLong4501",
"MaDaPrRoad90R",
"MaDaPrTree02",
"MaCoPrTr02",
"MaDaPrTree03",
"MaDaPrTree01",
"MaCoPrTr03",
"MaDaPrTree05",
"madafrsteelgroup_02",
"MaDaPrMine055",
"MaDaPrPump01",
"MaDaPrCliff02",
"DuDkRoPrPrison02",
"DuDkCoPrFirePot02",
"HarRuin06-02",
"HarPlant03",
"HarRuin06-01",
"HarRuin06",
"HarRuin04",
"HarRuin04-01",
"HarRuin07-01",
"HarRuin04-03",
"HarPlant02",
"HarPlant04",
"HarPlant06",
"HarPlant01",
"HarRuin04-02",
"HarRuin03-04",
"MaCoPrTr05",
"MaCoPrGr07-02",
"MaCoPrGr07",
"MaCoPrFl03-04",
"MaCoPrFl02-03",
"MaCoPrMu04",
"MaCoPrFl03-01",
"MaDaPrTree06",
"MaDaPrTree04",
"MaDaPrRevTree",
"MaFlPrTe02",
"MaCoPrTr15",
"MaFlPrMarseFountian",
"MaFlPrMarseTotem03",
"HarCamp10",
"HarCamp09",
"HarCamp11",
"HarCamp07",
"HarCamp01",
"HarCamp04",
"HarCamp02",
"HarCamp03",
"HarCamp08",
"HarCamp05",
"HarCamp06",
"HarRuin01-01",
"HarRuin01-03",
"HarRuin02-01",
"HarRuin01",
"HarRuin01-02",
"HarRuin02-02",
"HarRuin03-01",
"HarPlant05",
"HarRuin05-02",
"MaCoPrTr11",
"HarProp02",
"HarProp03",
"HarPlant09",
"HarPlant15",
"HarPlant16",
"DuDkCoPrFirewood",
"HarRuin05",
"HarRuin05-01",
"HarRuin02",
"HarRuin03-03",
"HarRuin03-02",
"HarRuin03",
"HarRuin01-04",
"HarProp01",
"CislandShfish02",
"CislandShfish03",
"CislandCoral03",
"CislandCoral02",
"HarTree07",
"HarTree08",
"MaCoPrTr10",
"DuDkCoPrPlant01",
"MaFlPrMarseFirePillar",
"MaCoPrMu06",
"HarTree05",
"HarTree06",
"HarTree04",
"CislandTree02",
"CislandTree01",
"CislandCabin03",
"MaCoPrGr06",
"CislandCabin01",
"CislandCabin02",
"CislandCabin05",
"HarTree03",
"HarPlant07",
"HarPlant11",
"HarPlant10",
"HarTree02",
"HarTree01",
"HarPlant12",
"HarPlant13",
"MaPrMu001",
"MaFlPrTr04",
"HarPlant08",
"HarProp04",
"Dunstatue_02",
"Dunstatue_01",
"Dundoor06",
"EstProp08",
"EstPlant01",
"EstPlant02",
"EstTree01",
"EstProp21",
"EstRock01",
"MaCoPrGr07-03",
"skylight",
"MaFlHaro01",
"MaFlHala01",
"MaFlHo01",
"MaFlRe01",
"MaFlWi01",
"MaFlHo02",
"MaFlCi001",
"MaCoPrTr01",
"MaFlPrBr03",
"MaFlSt001",
"MaFlReq01",
"MaFlPrGe01",
"MaKoGe01",
"MaFlHala02",
"MaFlAr01",
"MaFlPrFe02",
"MaCoPrGr05",
"MaFIPrLa02",
"MaFlPrSi04",
"MaFlPrSi02",
"MaCoPrMu05",
"MaPrMu002",
"MaPrSt001",
"MaCoPrFl02-04",
"MaCoPrFl03-03",
"MaFlPrBenc01",
"MaFlPrSi01",
"MaFlPrSi05",
"MaFlPrCa01",
"MaCoPrGr07-04",
"MaFlPrSi03",
"MaFlPrLa01",
"MaCoPrOi",
"MaFlReq01-01",
"MaKoGe03",
"MaSaSlope03",
"MaRiPrPrJoint01",
"MaRiPrCeiling01",
"MaKoGe02",
"DuDkCoPrBox01_01",
"genlodestar02Coll",
"HarPlant14",
"HarRock03",
"HarRock01",
"HarRock02",
"EstCamp05",
"EstCamp06",
"EstProp02",
"EstProp03",
"EstProp04",
"EstProp01",
"EstCamp07",
"EstProp05",
"EstProp06",
"EstProp07",
"EstProp10",
"EstCamp08",
"EstProp09",
"EstCamp10",
"EstCamp11",
"EstProp11",
"EstCamp04",
"EstCamp09",
"EstProp16",
"EstProp19",
"EstProp20",
"EstRock03",
"EstRock04",
"EstRock02",
"MaFlFo001",
"MaCoPrStWa04",
"MaCoPrStJo01",
"MaCoPrViaduct01-1",
"MaflPrMarseRoot02",
"MaflPrMarseEnter",
"MaFlPrMarseTorch01",
"MaSaPrDoSt01",
"MaSaPrDoSt01-02",
"MaSaPuScarecrow01",
"MaPrPumpstem01",
"MaSaPuHouse02",
"MaSaPuHouse03",
"MaSaPuFence01",
"MaSaPuHead02",
"MaSaPuHead03",
"MaSaPuHead04",
"MaSaPumkinPole01",
"MaSaPuFence02",
"skylight01",
"MaSaHo03",
"EstProp14",
"EstProp15",
"MaSaPrThTr01",
"MaSaPrBridge01",
"MaSaPrStLi01",
"MaSaPuHead",
"MaSaPuHouse01",
"MaSaPrCiEn01",
"MaSaSaHa01",
"MaSaBkSide02",
"MaSaBkInLe01",
"MaSaBkInRi01",
"MaSaBkSide03",
"MaSaPrFlag02",
"MaSaFightingGround",
"MaPrSmCr02",
"MaSaHo06",
"MaSaBkSide01",
"MaSaSlope05",
"MaSaSlope01",
"MaSaSlope04",
"MaSaSlope02",
"MaSaHo05",
"MaSaAr01",
"MaSaGe01",
"MaSaHo02",
"MaSaHo10",
"MaSaHo01",
"MaSaBkRouOutLe02",
"MaSaHo04",
"MaSaRestaurant",
"MaSaBkDiagonal02",
"MaSaBkDiaInRi01",
"MaSaBkDiagonal03",
"MaSaReq01",
"MaSaPrSupport01",
"MaSaBkDiaInLe01",
"MaSaBkRouOutLe03",
"MaSaBkOutRi01",
"MaSaPrWharf02",
"MaSaBkRouOutRi01",
"MaSaPrWharf01",
"MaSaBkOutLe01",
"MaSaBkRouOutLe01",
"MaSaBkRouOutRi02",
"MaSaBkRouInLe03",
"MaSaHo14",
"MaSaPrCr01",
"MaSaMagic01",
"MaSaBkRouInRi01",
"MaSaBkRouInLe01",
"MaSaBkRouInRi02",
"MaSaBkDiaOutLe01",
"MaSaprFlowerBed",
"aaaa",
"MaSaReq01-01",
"MaFlPrMarsefountain",
"DuDkCoPrPlant02",
"MaSaPrLi01",
"DuDkTrPrEgg01",
"MaRiPrFourProp02",
"MaRiPrPrup02",
"MaRiPr10",
"MaRiPrTwoProp02",
"MaRiPrBrokenProp01",
"MaRiPrBrokenProp02",
"MaRiPrBlock01",
"MaRiPrBlock02",
"MaRiPrTwoProp01",
"MaRiPrPrJoint02",
"MaRiPrMiddleProp01",
"MaRiPrMiddleProp02",
"MaRiPrFourProp03",
"MaRiPr11",
"MaRiPrBrokenBlock01",
"MaRiPrRootProp02",
"MaRiPrBrokenBlock02",
"MaRiPrPrup03",
"MaRiPrRootProp01",
"MaRiPrCeiling02",
"MaFlPrMarseRuFountian"

]
can_not_find = []
for o3d_name in kebaras:
    lower_prefix  ="obj_"+o3d_name.lower() 
    full_o3d_name =lower_prefix + filter_o3d
    full_sfx_name = lower_prefix + filter_sfx
    if full_o3d_name not in src_o3d_files and full_sfx_name not in src_sfx_files:
        print(o3d_name, full_o3d_name, full_sfx_name, '找不到对应的')
        can_not_find.append(o3d_name)
    


print(len(can_not_find))