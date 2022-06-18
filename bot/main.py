import os
import discord
import random

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

gift = 0xFCEEC2
big = 0x1B4C84
mega = 0xFFD046
lowships = ['Admiral Makarov', 'Agincourt', 'Aigle', 'Anshan', 'Arizona', 'Ark Royal', 'Ashitaka', 'Atlanta', 'Boise', 'Błyskawica', 'California', 'De Grasse', "Duca d'Aosta", 'Duca degli Abruzzi', 'Duke of York', 'Dunkerque', 'Exeter', 'Florida', 'Gallant', 'Genova', 'Gorizia', 'Hill', 'Hood', 'Huanghe', 'Hyūga', 'Indianapolis', 'Ise', 'Juruá', 'Kirov', 'Krasny Krym', 'Lazo', 'Leningrad', 'Leone', 'London', 'Marblehead', 'Marblehead Lima', 'Mikoyan', 'Molotov', 'Monaghan', 'Murmansk', 'Mutsu', 'Mysore', 'München', 'Nueve de Julio', 'Okhotnik', 'Oktyabrskaya Revolutsiya', 'Perth', 'Poltava', 'Prinz Eitel Friedrich', 'Scharnhorst', 'Sims', 'Siroco', 'Strasbourg', 'Texas', 'Viribus Unitis', 'W. Virginia 1941', 'Warspite', 'Weimar', 'Yahagi', 'Yukon', 'Yūdachi']
lowshipsdict = {'Admiral Makarov': 'https://cdn.discordapp.com/attachments/922286460068061194/922314819217010698/AdmiralMakarov.png', 'Agincourt': 'https://cdn.discordapp.com/attachments/922286460068061194/922314819447685121/Agincourt.png', 'Aigle': 'https://media.discordapp.net/attachments/922286460068061194/922314819644837918/Aigle.png', 'Anshan': 'https://media.discordapp.net/attachments/922286460068061194/922314819921670184/Anshan.png', 'Arizona': 'https://media.discordapp.net/attachments/922286460068061194/922314820122980402/Arizona.png', 'Ark Royal': 'https://media.discordapp.net/attachments/922286460068061194/922314820341096448/ArkRoyal.png', 'Ashitaka': 'https://media.discordapp.net/attachments/922286460068061194/922314820567564288/Ashitaka.png', 'Atlanta': 'https://media.discordapp.net/attachments/922286460068061194/922314820798271539/Atlanta.png', 'Boise': 'https://media.discordapp.net/attachments/922286460068061194/922314821431590972/Boise.png', 'Błyskawica': 'https://cdn.discordapp.com/attachments/922286460068061194/922314821129605140/Byskawica.png', 'California': 'https://cdn.discordapp.com/attachments/922286460068061194/922317417131147275/California.png', 'De Grasse': 'https://media.discordapp.net/attachments/922286460068061194/922317417366044742/DeGrasse.png', 'Duca d\'Aosta': 'https://media.discordapp.net/attachments/922286460068061194/922317417575747614/DucadAosta.png', 'Duca degli Abruzzi': 'https://media.discordapp.net/attachments/922286460068061194/922317417823232060/DucadegliAbruzzi.png', 'Duke of York': 'https://media.discordapp.net/attachments/922286460068061194/922317418112614401/DukeofYork.png', 'Dunkerque': 'https://media.discordapp.net/attachments/922286460068061194/922317418322346014/Dunkerque.png', 'Exeter': 'https://media.discordapp.net/attachments/922286460068061194/922317418506911853/Exeter.png', 'Florida': 'https://media.discordapp.net/attachments/922286460068061194/922317418699841646/Florida.png', 'Gallant': 'https://media.discordapp.net/attachments/922286460068061194/922317418913734667/Gallant.png', 'Genova': 'https://media.discordapp.net/attachments/922286460068061194/922317419215736882/Genova.png', 'Gorizia': 'https://cdn.discordapp.com/attachments/922286460068061194/922318088953798666/Gorizia.png', 'Hill': 'https://media.discordapp.net/attachments/922286460068061194/922318089289355304/Hill.png', 'Hood': 'https://cdn.discordapp.com/attachments/922286460068061194/922318086315606096/Hood.png', 'Huanghe': 'https://cdn.discordapp.com/attachments/922286460068061194/922318086642741288/Huanghe.png', 'Hyūga': 'https://media.discordapp.net/attachments/922286460068061194/922318087028604968/Hyuga.png', 'Indianapolis': 'https://media.discordapp.net/attachments/922286460068061194/922318087250919474/Indianapolis.png', 'Ise': 'https://media.discordapp.net/attachments/922286460068061194/922318087741661184/Ise.png', 'Juruá': 'https://cdn.discordapp.com/attachments/922286460068061194/922318088010080256/Jurua.png', 'Kirov': 'https://media.discordapp.net/attachments/922286460068061194/922318088249167882/Kirov.png', 'Krasny Krym': 'https://media.discordapp.net/attachments/922286460068061194/922318088551149608/KrasnyKrym.png', 'Lazo': 'https://media.discordapp.net/attachments/922286460068061194/922318787666133083/Lazo.png', 'Leningrad': 'https://media.discordapp.net/attachments/922286460068061194/922318787888422993/Leningrad.png', 'Leone': 'https://media.discordapp.net/attachments/922286460068061194/922318788119113728/Leone.png', 'London': 'https://cdn.discordapp.com/attachments/922286460068061194/922318788328820787/London.png', 'Marblehead': 'https://media.discordapp.net/attachments/922286460068061194/922318788635029524/Marblehead.png', 'Marblehead Lima': 'https://media.discordapp.net/attachments/922286460068061194/922318788840521778/MarbleheadLima.png', 'Mikoyan': 'https://media.discordapp.net/attachments/922286460068061194/922318789058650173/Mikoyan.png', 'Molotov': 'https://cdn.discordapp.com/attachments/922286460068061194/922318789314510918/Molotov.png', 'Monaghan': 'https://cdn.discordapp.com/attachments/922286460068061194/922318789520003083/Monaghan.png', 'Murmansk': 'https://media.discordapp.net/attachments/922286460068061194/922319353100238918/Murmansk.png', 'Mutsu': 'https://media.discordapp.net/attachments/922286460068061194/922319353335128074/Mutsu.png', 'Mysore': 'https://cdn.discordapp.com/attachments/922286460068061194/922319353691660298/Mysore.png', 'München': 'https://cdn.discordapp.com/attachments/922286460068061194/922318789771685908/Munchen.png', 'Nueve de Julio': 'https://cdn.discordapp.com/attachments/922286460068061194/922319353913962576/NuevedeJulio.png', 'Okhotnik': 'https://cdn.discordapp.com/attachments/922286460068061194/922319354174013440/Okhotnik.png', 'Oktyabrskaya Revolutsiya': 'https://cdn.discordapp.com/attachments/922286460068061194/922319354484379658/OktyabrskayaRevolutsiya.png', 'Perth': 'https://cdn.discordapp.com/attachments/922286460068061194/922319354861858876/Perth.png', 'Poltava': 'https://cdn.discordapp.com/attachments/922286460068061194/922319355247751168/Poltava.png', 'Prinz Eitel Friedrich': 'https://cdn.discordapp.com/attachments/922286460068061194/922319355545542666/PrinzEitelFriedrich.png', 'Scharnhorst': 'https://cdn.discordapp.com/attachments/922286460068061194/922319355943997460/Scharnhorst.png', 'Sims': 'https://cdn.discordapp.com/attachments/922286460068061194/922319779916828733/Sims.png', 'Siroco': 'https://cdn.discordapp.com/attachments/922286460068061194/922319780093001728/Siroco.png', 'Strasbourg': 'https://cdn.discordapp.com/attachments/922286460068061194/922319780323680317/Strasbourg.png', 'Texas': 'https://cdn.discordapp.com/attachments/922286460068061194/922319780579520532/Texas.png', 'Viribus Unitis': 'https://cdn.discordapp.com/attachments/922286460068061194/922319780814409818/ViribusUnitis.png', 'W. Virginia 1941': 'https://cdn.discordapp.com/attachments/922286460068061194/922319781066051664/W.Virginia1941.png', 'Warspite': 'https://cdn.discordapp.com/attachments/922286460068061194/922319781296742460/Warspite.png', 'Weimar': 'https://cdn.discordapp.com/attachments/922286460068061194/922319781552599050/Weimar.png', 'Yahagi': 'https://cdn.discordapp.com/attachments/922286460068061194/922319781753942116/Yahagi.png', 'Yukon': 'https://cdn.discordapp.com/attachments/922286460068061194/922320235640524821/Yukon.png', 'Yūdachi': 'https://cdn.discordapp.com/attachments/922286460068061194/922319781921689681/Yudachi.png'}
midships = ['Ägir', 'Alabama', 'Atago', 'Azuma', 'Bayard', "Belfast '43", 'Borodino', 'Champagne', 'Cheshire', 'Congress', 'Constellation', 'Cossack', 'Fenyang', 'Flandre', 'Gascogne', 'Graf Zeppelin', 'Groningen', 'Indomitable', 'Irian', 'Kaga', 'Kidd', 'Kii', 'Le Terrible', 'Loyang', 'Mainz', 'Marco Polo', 'Ochakov', 'Orkan', 'Pommern', 'Prinz Eugen', 'Pyotr Bagration', 'Roma', 'Saipan', 'Siliwangi', "Tiger '59", 'Tirpitz', 'Tone', 'Vanguard', 'Wichita', 'Z-35', 'Z-44']
midshipsdict = {'Ägir': 'https://cdn.discordapp.com/attachments/922286460068061194/922320626457395220/Agir.png', 'Alabama': 'https://cdn.discordapp.com/attachments/922286460068061194/922320626704863252/Alabama.png', 'Atago': 'https://cdn.discordapp.com/attachments/922286460068061194/922320626931339265/Atago.png', 'Azuma': 'https://cdn.discordapp.com/attachments/922286460068061194/922320624754511902/Azuma.png', 'Bayard': 'https://cdn.discordapp.com/attachments/922286460068061194/922320625018757151/Bayard.png', 'Belfast \'43': 'https://cdn.discordapp.com/attachments/922286460068061194/922320625266229328/Belfast43.png', 'Borodino': 'https://cdn.discordapp.com/attachments/922286460068061194/922320625559826472/Borodino.png', 'Champagne': 'https://cdn.discordapp.com/attachments/922286460068061194/922320625845014539/Champagne.png', 'Cheshire': 'https://cdn.discordapp.com/attachments/922286460068061194/922320626025373726/Cheshire.png', 'Congress': 'https://media.discordapp.net/attachments/922286460068061194/922320626272862238/Congress.png', 'Constellation': 'https://cdn.discordapp.com/attachments/922286460068061194/922321131879399424/Constellation.png', 'Cossack': 'https://cdn.discordapp.com/attachments/922286460068061194/922321132080750702/Cossack.png', 'Fenyang': 'https://cdn.discordapp.com/attachments/922286460068061194/922321132248510484/Fenyang.png', 'Flandre': 'https://cdn.discordapp.com/attachments/922286460068061194/922321132407889970/Flandre.png', 'Gascogne': 'https://cdn.discordapp.com/attachments/922286460068061194/922321132642795630/Gascogne.png', 'Graf Zeppelin': 'https://cdn.discordapp.com/attachments/922286460068061194/922321132844089344/GrafZeppelin.png', 'Groningen': 'https://cdn.discordapp.com/attachments/922286460068061194/922321133041246218/Groningen.png', 'Indomitable': 'https://cdn.discordapp.com/attachments/922286460068061194/922321133280329798/Indomitable.png', 'Irian': 'https://cdn.discordapp.com/attachments/922286460068061194/922321133544538152/Irian.png', 'Kaga': 'https://cdn.discordapp.com/attachments/922286460068061194/922321133779443722/Kaga.png', 'Kidd': 'https://cdn.discordapp.com/attachments/922286460068061194/922321521471528960/Kidd.png', 'Kii': 'https://cdn.discordapp.com/attachments/922286460068061194/922321521702228038/Kii.png', 'Le Terrible': 'https://cdn.discordapp.com/attachments/922286460068061194/922321521916129280/LeTerrible.png', 'Loyang': 'https://cdn.discordapp.com/attachments/922286460068061194/922321522209747034/Loyang.png', 'Mainz': 'https://cdn.discordapp.com/attachments/922286460068061194/922321522578841600/Mainz.png', 'Marco Polo': 'https://cdn.discordapp.com/attachments/922286460068061194/922321522843078716/MarcoPolo.png', 'Ochakov': 'https://cdn.discordapp.com/attachments/922286460068061194/922321523057000448/Ochakov.png', 'Orkan': 'https://cdn.discordapp.com/attachments/922286460068061194/922321523279294514/Orkan.png', 'Pommern': 'https://cdn.discordapp.com/attachments/922286460068061194/922321523455451136/Pommern.png', 'Prinz Eugen': 'https://cdn.discordapp.com/attachments/922286460068061194/922321523681919046/PrinzEugen.png', 'Pyotr Bagration': 'https://cdn.discordapp.com/attachments/922286460068061194/922321976054411364/PyotrBagration.png', 'Roma': 'https://cdn.discordapp.com/attachments/922286460068061194/922321976335413388/Roma.png', 'Saipan': 'https://cdn.discordapp.com/attachments/922286460068061194/922321976733876224/Saipan.png', 'Siliwangi': 'https://cdn.discordapp.com/attachments/922286460068061194/922321977061048371/Siliwangi.png', 'Tiger \'59': 'https://cdn.discordapp.com/attachments/922286460068061194/922321977291702302/Tiger59.png', 'Tirpitz': 'https://cdn.discordapp.com/attachments/922286460068061194/922321977518202930/Tirpitz.png', 'Tone': 'https://cdn.discordapp.com/attachments/922286460068061194/922321977744703548/Tone.png', 'Vanguard': 'https://cdn.discordapp.com/attachments/922286460068061194/922321978097041478/Vanguard.png', 'Wichita': 'https://cdn.discordapp.com/attachments/922286460068061194/922321978378031104/Wichita.png', 'Z-35': 'https://cdn.discordapp.com/attachments/922286460068061194/922321978621304832/Z-35.png', 'Z-44': 'https://cdn.discordapp.com/attachments/922286460068061194/922322404703862794/Z-44.png'}
rareships = ['Admiral Graf Spee', 'Alaska', 'Asashio', 'Belfast', 'Benham', 'Enterprise', 'Erich Loewenhardt', 'Flint', 'Friesland', 'Georgia', 'Haida', 'Hayate', 'Jean Bart', 'Kronshtadt', 'Lenin', 'Marceau', 'Massachusetts', 'Max Immelmann', 'Mikhail Kutuzov', 'Missouri', 'Moskva', 'Musashi', 'Napoli', 'Nelson', 'Neustrashimy', 'Salem', 'Smolensk', 'Småland', 'T-61', 'Thunderer', 'Yoshino', 'Z-39']
rareshipsdict = {'Admiral Graf Spee': 'https://cdn.discordapp.com/attachments/922286460068061194/922322637139611668/AdmiralGrafSpee.png', 'Alaska': 'https://cdn.discordapp.com/attachments/922286460068061194/922322637328384040/Alaska.png', 'Asashio': 'https://cdn.discordapp.com/attachments/922286460068061194/922322637538074634/Asashio.png', 'Belfast': 'https://cdn.discordapp.com/attachments/922286460068061194/922322637768773642/Belfast.png', 'Benham': 'https://cdn.discordapp.com/attachments/922286460068061194/922322637974274048/Benham.png', 'Enterprise': 'https://cdn.discordapp.com/attachments/922286460068061194/922322638150467654/Enterprise.png', 'Erich Loewenhardt': 'https://cdn.discordapp.com/attachments/922286460068061194/922322638347575456/ErichLoewenhardt.png', 'Flint': 'https://cdn.discordapp.com/attachments/922286460068061194/922322638553104494/Flint.png', 'Friesland': 'https://cdn.discordapp.com/attachments/922286460068061194/922322638779600946/Friesland.png', 'Georgia': 'https://cdn.discordapp.com/attachments/922286460068061194/922322639006085130/Georgia.png', 'Haida': 'https://cdn.discordapp.com/attachments/922286460068061194/922323019282649158/Haida.png', 'Hayate': 'https://cdn.discordapp.com/attachments/922286460068061194/922323019504951336/Hayate.png', 'Jean Bart': 'https://cdn.discordapp.com/attachments/922286460068061194/922323019718869022/JeanBart.png', 'Kronshtadt': 'https://cdn.discordapp.com/attachments/922286460068061194/922323019886645298/Kronshtadt.png', 'Lenin': 'https://cdn.discordapp.com/attachments/922286460068061194/922323020058595338/Lenin.png', 'Marceau': 'https://cdn.discordapp.com/attachments/922286460068061194/922323020205416518/Marceau.png', 'Massachusetts': 'https://cdn.discordapp.com/attachments/922286460068061194/922323020406718484/Massachusetts.png', 'Max Immelmann': 'https://cdn.discordapp.com/attachments/922286460068061194/922323020587085854/MaxImmelman.png', 'Mikhail Kutuzov': 'https://cdn.discordapp.com/attachments/922286460068061194/922323020792623144/MikhailKutuzov.png', 'Missouri': 'https://cdn.discordapp.com/attachments/922286460068061194/922323020981370930/Missouri.png', 'Moskva': 'https://cdn.discordapp.com/attachments/922286460068061194/922323380055711794/Moskva.png', 'Musashi': 'https://cdn.discordapp.com/attachments/922286460068061194/922323380252852254/Musashi.png', 'Napoli': 'https://cdn.discordapp.com/attachments/922286460068061194/922323380479348776/Napoli.png', 'Nelson': 'https://cdn.discordapp.com/attachments/922286460068061194/922323380655517726/Nelson.png', 'Neustrashimy': 'https://cdn.discordapp.com/attachments/922286460068061194/922323380965892126/Neustrashimy.png', 'Salem': 'https://cdn.discordapp.com/attachments/922286460068061194/922323381318189077/Salem.png', 'Smolensk': 'https://cdn.discordapp.com/attachments/922286460068061194/922323381905403994/Smolensk.png', 'Småland': 'https://cdn.discordapp.com/attachments/922286460068061194/922323381678919701/Smaland.png', 'T-61': 'https://cdn.discordapp.com/attachments/922286460068061194/922323382131908669/T-61.png', 'Thunderer': 'https://cdn.discordapp.com/attachments/922286460068061194/922323379816656946/Thunderer.png', 'Yoshino': 'https://cdn.discordapp.com/attachments/922286460068061194/922323743244714104/Yoshino.png', 'Z-39': 'https://cdn.discordapp.com/attachments/922286460068061194/922323743450218527/Z-39.png'}
specialsigs = {0: "Wyvern", 1: "Red Dragon", 2: "Dragon", 3: "Ouroboros", 4: "Scylla", 5: "Hydra", 6: "Basilisk", 7: "Leviathan"}
specialsigsURL = {0: "https://cdn.discordapp.com/attachments/922237568114905150/922280082020655125/5Wyvern.png", 1: "https://cdn.discordapp.com/attachments/922237568114905150/922280621731119134/5RedDragon.png", 2: "https://cdn.discordapp.com/attachments/922237568114905150/922279474412814376/5Dragon.png", 3: "https://cdn.discordapp.com/attachments/922237568114905150/922281482402295868/5Ouroboros.png", 4: "https://cdn.discordapp.com/attachments/922237568114905150/922281481571819541/5Scylla.png", 5: "https://cdn.discordapp.com/attachments/922237568114905150/922281481861214241/5Hydra.png", 6: "https://cdn.discordapp.com/attachments/922237568114905150/922281850687344650/5Basilisk.png", 7: "https://cdn.discordapp.com/attachments/922237568114905150/922281482045771827/5Leviathan.png"}
bigspecialsigsURL = {0: "https://cdn.discordapp.com/attachments/922286460068061194/922336203653652480/15Wyvern.png", 1: "https://cdn.discordapp.com/attachments/922286460068061194/922336204924534844/15RedDragon.png", 2: "https://cdn.discordapp.com/attachments/922286460068061194/922336204106657882/15Dragon.png", 3: "https://cdn.discordapp.com/attachments/922286460068061194/922336204735782912/15Ouroboros.png", 4: "https://cdn.discordapp.com/attachments/922286460068061194/922336203418783744/15Scylla.png", 5: "https://cdn.discordapp.com/attachments/922286460068061194/922336204345716806/15Hydra.png", 6: "https://cdn.discordapp.com/attachments/922286460068061194/922336203875942400/15Basilisk.png", 7: "https://cdn.discordapp.com/attachments/922286460068061194/922336204534468608/15Leviathan.png"}
megaspecialsigsURL = {0: "https://cdn.discordapp.com/attachments/922286460068061194/922344019600740423/30Wyvern.png", 1: "https://cdn.discordapp.com/attachments/922286460068061194/922344019063894057/30RedDragon.png", 2: "https://cdn.discordapp.com/attachments/922286460068061194/922344018220838912/30Dragon.png", 3: "https://cdn.discordapp.com/attachments/922286460068061194/922344018854158366/30Ouroboros.png", 4: "https://cdn.discordapp.com/attachments/922286460068061194/922344019328122880/30Scylla.png", 5: "https://media.discordapp.net/attachments/922286460068061194/922344018422136852/30Hydra.png", 6: "https://cdn.discordapp.com/attachments/922286460068061194/922344019806277652/30Basilisk.png", 7: "https://cdn.discordapp.com/attachments/922286460068061194/922344018640244796/30Leviathan.png"}
econsigs = {0: "Zulu", 1: "Equal Speed Charlie London", 2: "Zulu Hotel", 3: "Papa Papa"}
econsigsURL = {0: "https://cdn.discordapp.com/attachments/922237568114905150/922276336666562560/50Zulu.png", 1: "https://cdn.discordapp.com/attachments/922237568114905150/922277583796715560/50EqualSpeedCharlieLondon.png", 2: "https://cdn.discordapp.com/attachments/922237568114905150/922277993576013854/50ZuluHotel.png", 3: "https://cdn.discordapp.com/attachments/922237568114905150/922278254579171418/50PapaPapa.png"}
giftcamos = {0: "Frosty Fir Tree", 1: "New Year Streamer", 2: "Winter Strands", 3: "New Year", 4: "Type 3 - New Year"}
giftcamosURL = {0: "https://cdn.discordapp.com/attachments/922237568114905150/922285148123320330/4FrostyFirTree.png", 1: "https://cdn.discordapp.com/attachments/922237568114905150/922285148316246057/4NewYearStreamer.png", 2: "https://cdn.discordapp.com/attachments/922237568114905150/922285148484014131/4WinterStrands.png", 3: "https://cdn.discordapp.com/attachments/922237568114905150/922285951596757002/5NewYear.png", 4: "https://cdn.discordapp.com/attachments/922237568114905150/922285971226120272/5Type3NewYear.png"}
biggiftcamosURL = {0: "https://cdn.discordapp.com/attachments/922286460068061194/922332953730748536/12FrostyFirTree.png", 1: "https://media.discordapp.net/attachments/922286460068061194/922332954565427300/12NewYearStreamer.png", 2: "https://media.discordapp.net/attachments/922286460068061194/922332954968072242/12WinterStrands.png", 3: "https://cdn.discordapp.com/attachments/922286460068061194/922332953286176778/15NewYear.png", 4: "https://cdn.discordapp.com/attachments/922286460068061194/922332953483288717/15Type3NewYear.png"}
megaspecialcamos = {0: "Spring Sky", 1: "Asian Lantern", 2: "Mosaic"}
megaspecialcamosURL = {0: "https://cdn.discordapp.com/attachments/922286460068061194/922347010391171112/5SpringSky.png", 1: "https://cdn.discordapp.com/attachments/922286460068061194/922347205719891998/5AsianLantern.png", 2: "https://cdn.discordapp.com/attachments/922286460068061194/922347010105946142/5Mosaic.png"}
megacamos = {0: "Frosty Fir Tree", 1: "New Year Streamer", 2: "Winter Strands", 3: "Type 3 - New Year"}
megacamosURL = {0: "https://cdn.discordapp.com/attachments/922286460068061194/922347010659590164/20FrostyFirTree.png", 1: "https://cdn.discordapp.com/attachments/922286460068061194/922347010894467108/20NewYearStreamer.png", 2: "https://cdn.discordapp.com/attachments/922286460068061194/922347011171319828/20WinterStrands.png", 3: "https://cdn.discordapp.com/attachments/922286460068061194/922347012085653504/25Type3NewYear.png"}

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '!help'.lower() in message.content.lower() and message.content[0] == "!":
        await message.channel.send("Use !open [gift/big/mega] [number of containers (optional)]. Always assumes no ships are currently owned and will only account for duplicates and pity successes when opening more than one container at once.")
    if '!open'.lower() in message.content.lower() and message.content[0] == "!":
        words = message.content.lower().split()
        singularCheck = False
        if len(words) == 2:
            singularCheck = True
        else:
            if len(words) > 2:
                if words[2] == "1":
                    singularCheck = True
        if singularCheck:
            if 'gift' in words[1]:
                embeded = discord.Embed(title="**Gift Container**",color=gift)
                roll = random.random()
                if roll <= 0.025: #Ship
                    subroll = int(random.random() * 25)
                    if subroll <= 19: #Low Ship
                        shipname = lowships[int(random.random() * len(lowships))]
                        embeded.description = shipname
                        embeded.set_image(url=lowshipsdict[shipname])
                    elif subroll <= 23: #Mid Ship
                        shipname = midships[int(random.random() * len(midships))]
                        embeded.description = shipname
                        embeded.set_image(url=midshipsdict[shipname])
                    elif subroll <= 24: #Rare Ship
                        shipname = rareships[int(random.random() * len(rareships))]
                        embeded.description = shipname
                        embeded.set_image(url=rareshipsdict[shipname])
                elif roll <= 0.075: #500 Doubloons
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922237568114905150/922263968288997416/500Doubloons.png")
                elif roll <= 0.085: #30 Days Premium
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922237568114905150/922267197257187328/30Premium.png")
                elif roll <= 0.2: #4 New Year Sky Camos
                    embeded.description = "New Year Sky"
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922237568114905150/922284435062272060/4NewYearSky.png")
                elif roll <= 0.6: #50 Economic Signals
                    subroll = int(random.random() * 4)
                    embeded.description = econsigs[subroll]
                    embeded.set_image(url=econsigsURL[subroll])
                elif roll <= 0.85: #4 Frosty Fir Tree Camos, 4 New Year Streamer Camos, 4 Winter Strands Camos, 5 New Year Camos, or 5 Type 3 - New Year Camos
                    subroll = int(random.random() * 5)
                    embeded.description = giftcamos[subroll]
                    embeded.set_image(url=giftcamosURL[subroll])
                elif roll <= 0.92: #2500 Coal
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922237568114905150/922271300876124190/2500Coal.png")
                elif roll <= 1: #5 Special Signals
                    subroll = int(random.random() * 8)
                    embeded.description = specialsigs[subroll]
                    embeded.set_image(url=specialsigsURL[subroll])
                await message.channel.send(embed=embeded)
            elif 'big' in words[1]:
                embeded = discord.Embed(title="**Big Gift Container**",color=big)
                roll = random.random()
                #if roll <= 1:
                #    shipname = "Enterprise"
                #    embeded.description = shipname
                #    embeded.set_image(url=rareshipsdict[shipname])
                if roll <= 0.09: #Ship
                    subroll = int(random.random() * 18)
                    if subroll <= 13: #Low Ship
                        shipname = lowships[int(random.random() * len(lowships))]
                        embeded.description = shipname
                        embeded.set_image(url=lowshipsdict[shipname])
                    elif subroll <= 16: #Mid Ship
                        shipname = midships[int(random.random() * len(midships))]
                        embeded.description = shipname
                        embeded.set_image(url=midshipsdict[shipname])
                    elif subroll <= 17: #Rare Ship
                        shipname = rareships[int(random.random() * len(rareships))]
                        embeded.description = shipname
                        embeded.set_image(url=rareshipsdict[shipname])
                elif roll <= 0.14: #1500 Doubloons
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922237568114905150/922326688279437322/1500Doubloons.png")
                elif roll <= 0.15: #90 Days Premium
                    embeded.set_image(url="https://media.discordapp.net/attachments/922286460068061194/922327623537930240/90Premium.png")
                elif roll <= 0.31: #12 New Year Sky Camos
                    embeded.description = "New Year Sky"
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922286460068061194/922329712204865616/12NewYearSky.png")
                elif roll <= 0.61: #12 Frosty Fir Tree Camos, 12 New Year Streamer Camos, 12 Winter Strands Camos, 15 New Year Camos, or 15 Type 3 - New Year Camos
                    subroll = int(random.random() * 5)
                    embeded.description = giftcamos[subroll]
                    embeded.set_image(url=biggiftcamosURL[subroll])
                elif roll <= 0.68: #7500 Coal
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922286460068061194/922332979907403806/7500Coal.png")
                elif roll <= 1: #15 Special Signals
                    subroll = int(random.random() * 8)
                    embeded.description = specialsigs[subroll]
                    embeded.set_image(url=bigspecialsigsURL[subroll])
                await message.channel.send(embed=embeded)
            elif 'mega' in words[1]:
                embeded = discord.Embed(title="**Mega Gift Container**",color=mega)
                roll = random.random()
                if roll <= 0.16: #Ship
                    subroll = int(random.random() * 16)
                    if subroll <= 11: #Low Ship
                        shipname = lowships[int(random.random() * len(lowships))]
                        embeded.description = shipname
                        embeded.set_image(url=lowshipsdict[shipname])
                    elif subroll <= 14: #Mid Ship
                        shipname = midships[int(random.random() * len(midships))]
                        embeded.description = shipname
                        embeded.set_image(url=midshipsdict[shipname])
                    elif subroll <= 15: #Rare Ship
                        shipname = rareships[int(random.random() * len(rareships))]
                        embeded.description = shipname
                        embeded.set_image(url=rareshipsdict[shipname])
                elif roll <= 0.21: #2500 Doubloons
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922286460068061194/922347026946080778/2500Doubloons.png")
                elif roll <= 0.22: #180 Days Premium
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922286460068061194/922347026715402271/180Premium.png")
                elif roll <= 0.32: #20 New Year Sky Camos
                    embeded.description = "New Year Sky"
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922286460068061194/922347903303958538/20NewYearSky.png")
                elif roll <= 0.35: #20 Frosty Fir Tree Camos, 20 New Year Streamer Camos, 20 Winter Strands Camos, or 25 Type 3 - New Year Camos
                    subroll = int(random.random() * 4)
                    embeded.description = megacamos[subroll]
                    embeded.set_image(url=megacamosURL[subroll])
                elif roll <= 0.42: #12500 Coal
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922286460068061194/922347027243868230/12500Coal.png")
                elif roll <= 0.82: #30 Special Signals
                    subroll = int(random.random() * 8)
                    embeded.description = specialsigs[subroll]
                    embeded.set_image(url=megaspecialsigsURL[subroll])
                elif roll <= 0.85: #25 New Year Camos
                    embeded.description = "25 New Year Camos"
                    embeded.set_image(url="https://cdn.discordapp.com/attachments/922286460068061194/922370874588426281/25NewYear.png")
                elif roll <= 1: #5 Spring Sky, Asian Lantern, or Mosaic
                    subroll = int(random.random() * 3)
                    embeded.description = megaspecialcamos[subroll]
                    embeded.set_image(url=megaspecialcamosURL[subroll])
                await message.channel.send(embed=embeded)
            else:
                await message.channel.send("Invalid crate type") 
        elif len(words) > 2 and words[2].isalnum():
            crates = int(words[2])
            if crates <= 1000 and crates > 1:
                embeded = None
                validrequest = True
                doubsAcc = 0
                coalAcc = 0
                steelAcc = 0
                premAcc = 0
                econsigsAcc = [0, 0, 0, 0]
                specialsigsAcc = [0, 0, 0, 0, 0, 0, 0, 0]
                camosAcc = [0, 0, 0, 0, 0]
                nysAcc = 0
                specialcamosAcc = [0, 0, 0]
                shipsAcc = []
                lastship = -1
                if 'gift' in words[1]:
                    embeded = discord.Embed(title= "**" + str(crates) + " Gift Containers**",color=gift)
                    for i in range(crates):
                        roll = random.random()
                        if roll <= 0.025 or i - lastship - 1 == 99: #Ship
                            lastship = i
                            if len(shipsAcc) == 134:
                                steelAcc += 250
                            else:
                                shipname = ""
                                subroll = int(random.random() * 25)
                                if subroll <= 19: #Low Ship
                                    shipname = lowships[int(random.random() * len(lowships))]
                                elif subroll <= 23: #Mid Ship
                                    shipname = midships[int(random.random() * len(midships))]
                                elif subroll <= 24: #Rare Ship
                                    shipname = rareships[int(random.random() * len(rareships))]
                                while shipname in shipsAcc:
                                    subroll = int(random.random() * 25)
                                    if subroll <= 19: #Low Ship
                                        shipname = lowships[int(random.random() * len(lowships))]
                                    elif subroll <= 23: #Mid Ship
                                        shipname = midships[int(random.random() * len(midships))]
                                    elif subroll <= 24: #Rare Ship
                                        shipname = rareships[int(random.random() * len(rareships))]
                                shipsAcc.append(shipname)
                        elif roll <= 0.075: #500 Doubloons
                            doubsAcc += 500
                        elif roll <= 0.085: #30 Days Premium
                            premAcc += 30
                        elif roll <= 0.2: #4 New Year Sky Camos
                            nysAcc += 4
                        elif roll <= 0.6: #50 Economic Signals
                            subroll = int(random.random() * 4)
                            econsigsAcc[subroll] += 50
                        elif roll <= 0.85: #4 Frosty Fir Tree Camos, 4 New Year Streamer Camos, 4 Winter Strands Camos, 5 New Year Camos, or 5 Type 3 - New Year Camos
                            subroll = int(random.random() * 5)
                            if subroll <= 2:
                                camosAcc[subroll] += 4
                            else:
                                camosAcc[subroll] += 5
                        elif roll <= 0.92: #2500 Coal
                            coalAcc += 2500
                        elif roll <= 1: #5 Special Signals
                            subroll = int(random.random() * 8)
                            specialsigsAcc[subroll] += 5
                elif 'big' in words[1]:
                    embeded = discord.Embed(title= "**" + str(crates) + " Big Gift Containers**",color=big)
                    for i in range(crates):
                        shipname = ""
                        roll = random.random()
                        if roll <= 0.09 or i - lastship - 1 == 26: #Ship
                            lastship = i
                            if len(shipsAcc) == 134:
                                steelAcc += 750
                            else:
                                shipname = ""
                                subroll = int(random.random() * 18)
                                if subroll <= 13: #Low Ship
                                    shipname = lowships[int(random.random() * len(lowships))]
                                elif subroll <= 16: #Mid Ship
                                    shipname = midships[int(random.random() * len(midships))]
                                elif subroll <= 17: #Rare Ship
                                    shipname = rareships[int(random.random() * len(rareships))]
                                while shipname in shipsAcc:
                                    subroll = int(random.random() * 25)
                                    if subroll <= 13: #Low Ship
                                        shipname = lowships[int(random.random() * len(lowships))]
                                    elif subroll <= 16: #Mid Ship
                                        shipname = midships[int(random.random() * len(midships))]
                                    elif subroll <= 17: #Rare Ship
                                        shipname = rareships[int(random.random() * len(rareships))]
                            shipsAcc.append(shipname)
                        elif roll <= 0.14: #1500 Doubloons
                            doubsAcc += 1500
                        elif roll <= 0.15: #90 Days Premium
                            premAcc += 90
                        elif roll <= 0.31: #12 New Year Sky Camos
                            nysAcc += 12
                        elif roll <= 0.61: #12 Frosty Fir Tree Camos, 12 New Year Streamer Camos, 12 Winter Strands Camos, 15 New Year Camos, or 15 Type 3 - New Year Camos
                            subroll = int(random.random() * 5)
                            if subroll <= 2:
                                camosAcc[subroll] += 12
                            else:
                                camosAcc[subroll] += 15
                        elif roll <= 0.68: #7500 Coal
                            coalAcc += 7500
                        elif roll <= 1: #15 Special Signals
                            subroll = int(random.random() * 8)
                            specialsigsAcc[subroll] += 15
                elif 'mega' in words[1]:
                    embeded = discord.Embed(title= "**" + str(crates) + " Mega Gift Containers**",color=mega)
                    for i in range(crates):
                        roll = random.random()
                        if roll <= 0.16 or i - lastship - 1 == 14: #Ship
                            lastship = i
                            if len(shipsAcc) == 134:
                                steelAcc += 250
                            else:
                                shipname = ""
                                subroll = int(random.random() * 16)
                                if subroll <= 11: #Low Ship
                                    shipname = lowships[int(random.random() * len(lowships))]
                                elif subroll <= 14: #Mid Ship
                                    shipname = midships[int(random.random() * len(midships))]
                                elif subroll <= 15: #Rare Ship
                                    shipname = rareships[int(random.random() * len(rareships))]
                                while shipname in shipsAcc:
                                    subroll = int(random.random() * 25)
                                    if subroll <= 11: #Low Ship
                                        shipname = lowships[int(random.random() * len(lowships))]
                                    elif subroll <= 14: #Mid Ship
                                        shipname = midships[int(random.random() * len(midships))]
                                    elif subroll <= 15: #Rare Ship
                                        shipname = rareships[int(random.random() * len(rareships))]
                                shipsAcc.append(shipname)
                        elif roll <= 0.21: #2500 Doubloons
                            doubsAcc += 2500
                        elif roll <= 0.22: #180 Days Premium
                            premAcc += 180
                        elif roll <= 0.32: #20 New Year Sky Camos
                            nysAcc += 20
                        elif roll <= 0.35: #20 Frosty Fir Tree Camos, 20 New Year Streamer Camos, 20 Winter Strands Camos, or 25 Type 3 - New Year Camos
                            subroll = int(random.random() * 4)
                            if subroll <= 2:
                                camosAcc[subroll] += 20
                            else:
                                camosAcc[4] += 25
                        elif roll <= 0.42: #12500 Coal
                            coalAcc += 12500
                        elif roll <= 0.82: #30 Special Signals
                            subroll = int(random.random() * 8)
                            specialsigsAcc[subroll] += 30
                        elif roll <= 0.85: #25 New Year Camos
                            camosAcc[3] += 25
                        elif roll <= 1: #5 Spring Sky, Asian Lantern, or Mosaic
                            subroll = int(random.random() * 3)
                            specialcamosAcc[subroll] += 5
                else:
                    validrequest = False
                    await message.channel.send("Invalid crate type") 
                if validrequest:
                    if len(shipsAcc) > 0:
                        shipsAcc.sort()
                        lowshipstring = ""
                        lowshipscount = 0
                        midshipstring = ""
                        midshipscount = 0
                        rareshipstring = ""
                        rareshipscount = 0
                        for i in shipsAcc:
                            if i in lowships:
                                if len(lowshipstring) == 0:
                                    lowshipstring = i
                                else:
                                    lowshipstring += ", " + i
                                lowshipscount += 1
                            elif i in midships:
                                if len(midshipstring) == 0:
                                    midshipstring = i
                                else:
                                    midshipstring += ", " + i
                                midshipscount += 1
                            elif i in rareships:
                                if len(rareshipstring) == 0:
                                    rareshipstring = i
                                else:
                                    rareshipstring += ", " + i
                                rareshipscount += 1
                        if len(rareshipstring) > 0:
                            embeded.add_field(name="**Rare and Tier X Ships** (" + str(rareshipscount) + ")", value=rareshipstring, inline=False)
                        if len(midshipstring) > 0:
                            embeded.add_field(name="**Tier VIII and IX Ships** (" + str(midshipscount) + ")", value=midshipstring, inline=False)
                        if len(lowshipstring) > 0:
                            embeded.add_field(name="**Tier V-VII Ships** (" + str(lowshipscount) + ")", value=lowshipstring, inline=False)
                    if doubsAcc > 0:
                        embeded.add_field(name="**Doubloons**", value=str(doubsAcc), inline=False)
                    if premAcc > 0:
                        embeded.add_field(name="**Days of Premium**", value=str(premAcc), inline=False)
                    if coalAcc > 0:
                        embeded.add_field(name="**Coal**", value=str(coalAcc), inline=False)
                    if steelAcc > 0:
                        embeded.add_field(name="**Steel**", value=str(steelAcc), inline=False)
                    if camosAcc[0] > 0:
                        embeded.add_field(name="**Frosty Fir Tree Camos**", value=str(camosAcc[0]), inline=False)
                    if camosAcc[1] > 0:
                        embeded.add_field(name="**New Year Streamer Camos**", value=str(camosAcc[1]), inline=False)
                    if camosAcc[2] > 0:
                        embeded.add_field(name="**Winter Strands Camos**", value=str(camosAcc[2]), inline=False)
                    if camosAcc[3] > 0:
                        embeded.add_field(name="**New Year Camos**", value=str(camosAcc[3]), inline=False)
                    if camosAcc[4] > 0:
                        embeded.add_field(name="**Type 3 - New Year Camos**", value=str(camosAcc[4]), inline=False)
                    if nysAcc > 0:
                        embeded.add_field(name="**New Year Sky Camos**", value=str(nysAcc), inline=False)
client.run(TOKEN)