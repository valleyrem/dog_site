# -*- coding: utf-8 -*-
"""Breed history texts for the "History & origin" block (5 languages).

Keys are breed slugs. The command ``fill_history_content`` writes them into
``Dogs.history`` / ``history_ru`` / ``history_de`` / ``history_it`` /
``history_sr_latn``. Every dict ends with a marker comment so new breeds can
be appended without touching the rest of the file.
"""

HISTORY_EN = {
    "afghan-hound": (
        "The Afghan Hound is one of the oldest sighthound types, with carvings and "
        "writings suggesting a dog of this shape existed in Afghanistan and the "
        "surrounding mountains thousands of years ago. Local hunters used it to "
        "course hare and gazelle across rough, rocky ground, where speed alone was "
        "not enough. British officers brought the breed home in the late nineteenth "
        "century, and the first Afghan Hounds were shown in Britain in 1907. "
        "The Kennel Club recognised the breed in 1926, and its aristocratic look "
        "made it a fashion icon of the 1960s and 1970s."
    ),
    "airedale-terrier": (
        "The Airedale Terrier comes from the Aire valley in Yorkshire, where "
        "nineteenth-century workers crossed the now extinct Old English Black and "
        "Tan Terrier with the Otterhound. The aim was a dog that could hunt otter "
        "and rat, work alongside a gun and still guard the yard. It became known as "
        "the King of Terriers, and British soldiers used it as a messenger and "
        "sentry dog in the First World War. The breed was recognised in Britain in "
        "1886 and later spread as a family companion and police dog."
    ),
    "akita": (
        "The Akita has been bred in northern Japan for centuries and is tied to the "
        "mountain districts of Akita Prefecture, where it was used to hunt bear, "
        "boar and deer. Japanese tradition treated the breed as a symbol of good "
        "health and good fortune, and small statues of it are still given as gifts. "
        "After the Second World War the breed nearly disappeared and was restored "
        "from a small number of surviving lines. The best-known Akita, Hachiko, "
        "waited for his owner at a Tokyo station for almost ten years and is "
        "remembered with a bronze statue."
    ),
    "alaskan-malamute": (
        "The Alaskan Malamute takes its name from the Mahlemut Inuit people of "
        "Alaska, who kept heavy freight dogs long before Europeans arrived. These "
        "dogs hauled sledges loaded with meat, hides and camp gear, and they also "
        "worked in polar expeditions of the early twentieth century. During the "
        "Klondike gold rush the breed was crossed with smaller, faster sled dogs and "
        "almost lost its original type. Breeders in the 1920s and 1930s brought the "
        "heavy, powerful Malamute back, and it was recognised in the United States "
        "in 1935."
    ),
    "american-cocker-spaniel": (
        "The American Cocker Spaniel descends from dogs brought to North America "
        "from England in the nineteenth century, where the Cocker was still one "
        "breed with the English Cocker. American breeders wanted a smaller, "
        "silkier-coated dog for hunting woodcock in dense cover. The two types "
        "drifted apart, and the American Cocker was recognised as a separate breed "
        "in the United States in 1946. It became one of the most popular companion "
        "breeds of the twentieth century and the model for the Disney dog Lady."
    ),
    "american-eskimo-dog": (
        "The American Eskimo Dog descends from white spitz dogs taken to the "
        "United States by German immigrants in the nineteenth century. They worked "
        "in travelling circuses, where their tricks made the little white dog "
        "famous across the country. When anti-German feeling grew during the First "
        "World War, the name was changed from German Spitz to American Eskimo. The "
        "breed was recognised in the United States in 1995 and is still prized as a "
        "lively family dog and watchdog."
    ),
    "american-staffordshire-terrier": (
        "The American Staffordshire Terrier goes back to bull-and-terrier dogs "
        "brought to the United States from Britain in the nineteenth century. "
        "American breeders made a taller, heavier dog than the English original and "
        "used it as a farm and family dog as well as in the pit. It was first "
        "registered as the American Bull Terrier and later as the Staffordshire "
        "Terrier. The name American Staffordshire Terrier was adopted in 1969 to "
        "separate it from the English Staffordshire Bull Terrier, and the breed "
        "became a popular family companion."
    ),
    "anatolian-shepherd-dog": (
        "The Anatolian Shepherd Dog is an ancient livestock guardian from the "
        "plains of Anatolia in Turkey. For centuries it lived with shepherds and "
        "their flocks, guarding sheep against wolves and bears without herding "
        "them. The dogs were bred for endurance, independence and the ability to "
        "work alone in a harsh climate. Turkey began to record the breed in the "
        "1970s, and it spread to Europe and the United States as a working guardian "
        "and a calm, imposing family dog."
    ),
    "australian-shepherd": (
        "The Australian Shepherd was developed in the western United States, not in "
        "Australia, although its ancestors came from Basque and Australian herding "
        "dogs. Ranchers needed a dog that could move sheep and cattle over long "
        "distances and work in heat, dust and snow. The breed was kept by working "
        "families and rodeo performers, and the name came from the livestock and "
        "shepherds that arrived with Australian shipments. It was recognised in the "
        "United States in 1991 and is now one of the best-known herding breeds."
    ),
    "azawakh": (
        "The Azawakh is a sighthound of the Sahel, bred by the Tuareg and other "
        "nomadic peoples of Mali, Niger and Burkina Faso. It hunts gazelle and hare "
        "across open desert and guards the camp, living closely with people. The "
        "breed is named after the Azawakh valley, and its lean shape is adapted to "
        "heat and long distances. The first Azawakhs reached Europe in the 1970s, "
        "and the breed was recognised internationally in 1981."
    ),
    "barbado-da-terceira": (
        "The Barbado da Terceira comes from Terceira island in the Azores, where it "
        "was bred to work with cattle on rough volcanic ground. Island farmers "
        "needed a medium-sized dog that could herd, guard the property and be "
        "gentle with the family. The breed stayed almost unknown outside the Azores "
        "for centuries and was saved by local breeders in the twentieth century. "
        "Portugal recognised it nationally in 2004, and it is now a rare but "
        "steadily growing companion and herding dog."
    ),
    "basset-hound": (
        "The Basset Hound descends from French scent hounds kept by abbeys and "
        "noble households for hunting rabbit and deer. The short-legged, slow-"
        "moving type appeared in France in the sixteenth century and was refined in "
        "the nineteenth, when hunters wanted a dog that could be followed on foot. "
        "British breeders imported the breed in 1866 and gave it its modern look. "
        "The Basset Hound was recognised in Britain in 1880 and became a famous "
        "advertising and family dog in the twentieth century."
    ),
    "bedlington-terrier": (
        "The Bedlington Terrier was developed in the mining country of "
        "Northumberland, England, and named after the town of Bedlington. Miners "
        "and poachers used it to hunt rats, rabbits and otter, and it could squeeze "
        "through narrow burrows. Its lamb-like coat and curved back hide a tough "
        "terrier, and the breed was once known as the Rothbury Terrier. It was "
        "recognised in Britain in 1877 and later became a show dog and a family "
        "companion."
    ),
    "bichon-frise": (
        "The Bichon Frise descends from small white dogs carried around the "
        "Mediterranean by sailors and traders in the Middle Ages. The type was "
        "refined in France, where it became a favourite of the court and later of "
        "street performers and organ grinders. Its loose, curly coat and cheerful "
        "temper made it a popular circus dog. The breed was recognised in France in "
        "1933 and in the United States in 1972, and is now a much-loved companion."
    ),
    "black-and-tan-coonhound": (
        "The Black and Tan Coonhound was developed in the United States from "
        "European scent hounds brought by settlers, especially the Talbot Hound and "
        "the Bloodhound. Hunters needed a dog that could trail raccoon and bear "
        "through the night and then bay up a tree. The breed works entirely by nose "
        "and is famous for its deep, steady voice on the trail. It was recognised "
        "in the United States in 1945 and remains a specialist hunting dog."
    ),
    "bloodhound": (
        "The Bloodhound is one of the oldest scent hounds, with ancestors described "
        "in Europe as early as the seventh century and refined by monks in Belgium "
        "and France. The name refers to blooded, pure-bred stock rather than to "
        "blood itself. For centuries it has been used to trail deer, boar and, "
        "later, people, and its evidence has been accepted in courts. The breed was "
        "standardised in Britain in 1897 and is still the reference for "
        "scent-tracking work worldwide."
    ),
    "bolognese": (
        "The Bolognese is a small white companion dog from Bologna in Italy, and "
        "ancestors of this type appear in Italian art of the Renaissance. Noble "
        "families kept them as lap dogs and gave them as diplomatic gifts to other "
        "European courts. The breed nearly disappeared in the nineteenth century "
        "and was rebuilt from a few surviving lines in the twentieth. Italy "
        "recognised the Bolognese in 1956, and it is still rare outside its "
        "homeland."
    ),
    "border-collie": (
        "The Border Collie was formed on the border of England and Scotland, where "
        "shepherds needed a dog to move sheep on hills with a single command or "
        "whistle. Breeders selected for intelligence, stamina and, above all, a "
        "quiet, controlling stare that came to be called eye. The name was adopted "
        "in 1915; before that the dogs were known simply as working collies. The "
        "breed is still the standard for sheepdog trials, and one of its members, "
        "Chaser, learned the names of more than a thousand toys."
    ),
    "border-terrier": (
        "The Border Terrier comes from the Cheviot Hills between England and "
        "Scotland, where it worked with foxhounds and hunted foxes that threatened "
        "sheep. It had to be narrow enough to follow a fox into a burrow and tough "
        "enough to run with horses all day. The breed was shown first as the "
        "Coquetdale Terrier and took the name Border in 1880. It was recognised in "
        "Britain in 1920 and is still kept as a working terrier and a sturdy "
        "family dog."
    ),
    "borzoi": (
        "The Borzoi, or Russian Hunting Sighthound, was created by Russian nobles "
        "by crossing Arabian and Persian sighthounds with local thick-coated "
        "hunting dogs. It was used in wolf hunts, working in pairs or small packs "
        "alongside borzoi hunters on horseback. The breed was kept almost "
        "exclusively by the aristocracy, and the revolution of 1917 nearly ended "
        "it. Surviving dogs were exported in the 1920s, and the breed was "
        "recognised internationally in the twentieth century as an elegant show "
        "and companion dog."
    ),
    "boxer": (
        "The Boxer was developed in Germany in the nineteenth century from the "
        "Bullenbeisser and the English Bulldog. Munich breeders wanted a powerful "
        "guard and cattle dog with a short, clean head and a steady character. The "
        "first Boxer was registered in 1904, and the breed soon spread as a police "
        "and military dog. In the First World War it served as a messenger and "
        "sentry, and after the war it became one of the most popular family dogs in "
        "Europe and North America."
    ),
    "bulldog": (
        "The Bulldog descends from the old English mastiff-type dogs used for bull "
        "baiting, a cruel sport banned in Britain in 1835. When the sport ended, "
        "breeders turned the dog into a gentle companion and gave it the heavy, "
        "short-faced shape we know today. The first breed club was founded in 1875, "
        "and the Bulldog became a national symbol of Britain, compared in cartoons "
        "to the character of the country itself. Modern breeding focuses on health, "
        "breathing and mobility."
    ),
    "bull-terrier": (
        "The Bull Terrier was created in nineteenth-century England by crossing the "
        "old bull-and-terrier with the now extinct White English Terrier. James "
        "Hinks set out to build an all-white, athletic dog with an egg-shaped head, "
        "and the breed was recognised in Britain in 1887. Coloured dogs were added "
        "in the twentieth century and were registered as Staffordshire Bull "
        "Terriers. The Bull Terrier became famous as a sporting and army mascot and "
        "later as a stylish urban companion."
    ),
    "cane-corso": (
        "The Cane Corso comes from southern Italy and descends from the old Roman "
        "molosser dogs used for guarding, hunting and war. Its name refers to the "
        "Latin word for bodyguard, and for centuries it worked on farms, drove "
        "cattle and protected property. The breed nearly vanished after the Second "
        "World War and was saved by Italian enthusiasts in the 1970s. Italy drew up "
        "a standard in 1987, and the Cane Corso is now a popular guardian and "
        "family dog around the world."
    ),
    "catahoula-leopard-dog": (
        "The Catahoula Leopard Dog is the state dog of Louisiana and takes its name "
        "from Catahoula Parish. It was formed from dogs brought by Spanish "
        "explorers, French settlers and Native American stock, and its speckled, "
        "leopard-like coat is unique among working breeds. The dog was used to herd "
        "wild hogs and cattle in swamps and pine woods, working in packs. It was "
        "officially recognised as a breed in the United States in 1979 and is still "
        "chiefly a working dog."
    ),
    "cavalier-king-charles-spaniel": (
        "The Cavalier King Charles Spaniel revives the small toy spaniels painted "
        "beside European nobility in the sixteenth and seventeenth centuries. King "
        "Charles II was so fond of them that the type was named after him. By the "
        "twentieth century the flat-faced English Toy Spaniel had replaced the old "
        "look, and American breeders offered a prize for dogs with the long muzzle "
        "of the old paintings. The Cavalier was recognised in Britain in 1945 and "
        "has since become one of the most popular companion breeds."
    ),
    "collie-rough": (
        "The Collie Rough is a Scottish herding dog from the Highlands, where it "
        "worked with sheep on hills and in all weather. The breed was refined in "
        "the nineteenth century, and Queen Victoria's fondness for the dogs made "
        "them fashionable beyond Scotland. The name comes from the old Scottish "
        "word for a useful black and white sheepdog. The breed was recognised in "
        "Britain in 1874, and the novels and films about Lassie turned the Collie "
        "into a worldwide symbol of the loyal family dog."
    ),
    "czechoslovakian-wolfdog": (
        "The Czechoslovakian Wolfdog was created in 1955 as a military experiment "
        "in Czechoslovakia, crossing German Shepherd Dogs with Carpathian wolves. "
        "The aim was to combine the trainability of the shepherd with the stamina "
        "and senses of the wolf for border patrol work. The crossing was "
        "successful, but the dogs proved hard to train and were never used in large "
        "numbers by the army. The breed was recognised in Czechoslovakia in 1982 "
        "and internationally in 1999, and it is kept today as a demanding working "
        "and companion dog."
    ),
    "dachshund": (
        "The Dachshund was developed in Germany over several centuries from short-"
        "legged hunting dogs that could follow badgers and foxes into their dens. "
        "The name means badger dog, and the breed appears in German records from the "
        "fifteenth century. Three coat types and two sizes were bred for different "
        "quarry, and the dogs also worked in packs on boar and deer. It was "
        "recognised in Britain in 1881 and became a much-loved family companion, "
        "especially popular as the long-bodied, short-legged friend of the modern "
        "home."
    ),
    "dalmatian": (
        "The Dalmatian takes its name from the Adriatic region of Dalmatia, and "
        "dogs of this spotted type appear in paintings and church records from the "
        "seventeenth and eighteenth centuries. The breed was used as a carriage "
        "dog: it ran beside or under the axle, clearing the road and guarding the "
        "horses at inns. British breeders standardised it in the nineteenth century, "
        "and it was recognised in 1888. Its association with fire stations began "
        "when horse-drawn fire engines kept Dalmatians to calm and guide the horses."
    ),
    "dobermann": (
        "The Dobermann was created in the 1890s by Karl Friedrich Louis Dobermann, a "
        "German tax collector and dog catcher from Apolda. He needed a fearless, "
        "intelligent guard that could accompany him on dangerous rounds, and built "
        "the breed from several guarding and hunting types. The first breed club "
        "appeared in 1899, and the dog spread quickly as a police and military "
        "working breed. It was recognised internationally in the early twentieth "
        "century and remains one of the most respected protection and service dogs."
    ),
    "drever": (
        "The Drever is a Swedish scent hound bred from the Westphalian Dachsbracke "
        "and other German hunting dogs brought north in the nineteenth century. "
        "Swedish hunters wanted a short-legged, steady hound that could trail roe "
        "deer and hare through snow and thick forest at a pace a man could follow. "
        "For years it was called the Swedish Dachsbracke, and it was renamed the "
        "Drever in 1947. Sweden recognised the breed nationally, and it is still one "
        "of the country's most popular hunting dogs."
    ),
    "dutch-shepherd-dog": (
        "The Dutch Shepherd Dog is the herding breed of the Netherlands, bred in "
        "three coat types: short, long and wire-haired. Farmers kept them to move "
        "sheep and cattle, to guard the yard and to pull small carts, and they also "
        "worked as police and messenger dogs. The breed was standardised in 1898 "
        "with the founding of the Dutch club, and after the Second World War the "
        "numbers fell sharply. Serious breeding resumed in the 1970s, and today the "
        "breed is used in police and search work as well as in sport."
    ),
    "english-setter": (
        "The English Setter was developed over four hundred years in Britain from "
        "setting dogs that crouched when they found game, allowing hunters to drop a "
        "net over the birds. In the nineteenth century Edward Laverack and Purcell "
        "Llewellin shaped the two strains from which most modern setters descend. "
        "The breed was recognised in Britain in 1874. It is known for its gentle "
        "temper and its speckled, belton coat, and it still works as a pointing dog "
        "and a family companion."
    ),
    "french-bulldog": (
        "The French Bulldog began as a small English bulldog kept by lace workers in "
        "Nottingham, who took their dogs with them when they moved to France in the "
        "1860s. In Paris the dogs became a favourite of society and of artists, and "
        "French breeders selected for the upright bat ears and compact body. The "
        "breed was recognised in France in 1898 and in the United States in 1898 as "
        "well. It survived a near collapse in popularity in the early twentieth "
        "century and is today one of the most common companion breeds in the world."
    ),
    "german-shepherd-dog": (
        "The German Shepherd Dog was founded in 1899 by Max von Stephanitz, who "
        "wanted a working herding dog of great intelligence and stamina. He bought "
        "the dog Hektor, renamed him Horand von Grafrath, and with the club SV set "
        "out to prove the breed's worth in service. The dog spread quickly as a "
        "police, military and guide dog, and became famous in both world wars. It "
        "was recognised internationally in the early twentieth century and remains "
        "one of the most widely used working breeds."
    ),
    "german-shorthaired-pointer": (
        "The German Shorthaired Pointer comes from nineteenth-century Germany, where "
        "hunters needed one dog for everything: pointing, retrieving, tracking and "
        "water work. The breed was built from old German pointing dogs, hounds and "
        "water dogs, and Prince Albrecht zu Solms-Braunfels helped to guide its "
        "development. The first stud book was published in 1872. It was recognised "
        "in the United States in 1930 and is now one of the most versatile hunting "
        "breeds in the world."
    ),
    "german-spitz": (
        "The German Spitz belongs to the oldest dog family in central Europe, the "
        "spitz type that has been kept around farms and homes for centuries. The "
        "breed is divided by size into Wolfspitz, Giant, Medium, Miniature and "
        "Pomeranian, and all of them share the pointed ears, thick coat and curled "
        "tail. Spitz dogs worked as watchdogs, herders and companions, and their "
        "image appears in German art from the Middle Ages. The breed was "
        "standardised in Germany in 1899 and recognised internationally in the "
        "twentieth century."
    ),
    "golden-retriever": (
        "The Golden Retriever was created in the Scottish Highlands in the second "
        "half of the nineteenth century by Dudley Marjoribanks, later Lord "
        "Tweedmouth. He crossed a yellow wavy-coated retriever with the now extinct "
        "Tweed Water Spaniel to get a biddable dog for retrieving game from land "
        "and water. The first litter was whelped in 1868, and the line was kept "
        "private for decades. The breed was recognised in Britain in 1913 and has "
        "since become one of the world's favourite family, guide and search dogs."
    ),
    "great-dane": (
        "The Great Dane was developed in Germany from old mastiff and hunting dogs, "
        "and German breeders fixed the modern type in the late nineteenth century. "
        "Despite its English name, the breed is German: it was called the Deutsche "
        "Dogge, and in 1880 a committee in Berlin agreed on the first standard. The "
        "dog was bred to hunt boar on horseback and to guard estates, and its "
        "height and calm bearing earned it the nickname Apollo of Dogs. It was "
        "recognised internationally in the early twentieth century."
    ),
    "hovawart": (
        "The Hovawart is an old German farm dog whose name means keeper of the "
        "yard, and dogs of this type are mentioned in German law codes of the "
        "Middle Ages. The modern breed was rebuilt in the 1920s by breeders who "
        "searched the Black Forest and Harz regions for dogs that matched the old "
        "descriptions. They were crossed with German Shepherds, Newfoundlands and "
        "Leonbergers to fix the type. Germany recognised the Hovawart in 1937, and "
        "it is still kept mainly as a working guardian and family dog."
    ),
    "irish-wolfhound": (
        "The Irish Wolfhound is an ancient Irish sighthound used to hunt wolf, elk "
        "and boar, and it appears in Irish records and sagas from the first "
        "centuries AD. Irish chieftains gave the dogs as gifts to European and "
        "English kings, which helped to spread the breed and, later, to deplete it. "
        "By the nineteenth century wolves were gone and the breed was nearly "
        "extinct; Captain George Graham rebuilt it from surviving lines and "
        "similar sighthounds. It was recognised in Britain in 1886 and is the "
        "tallest of all dog breeds."
    ),
    "italian-sighthound": (
        "The Italian Sighthound, or Piccolo Levriero Italiano, is a small "
        "sighthound that appears in Italian art from the Roman period onward and "
        "was kept by noble families across the peninsula. It was used to course "
        "hare and rabbit and, above all, served as an elegant companion in the "
        "courts of Florence and Milan. The breed was standardised in Italy in 1928, "
        "and the first dogs reached Britain in the 1950s. Its fine build and quiet "
        "nature make it a popular apartment dog today."
    ),
    "italian-spinone": (
        "The Italian Spinone is a rough-coated gundog from Piedmont and Lombardy, "
        "where it has worked for centuries in the fields and marshes of northern "
        "Italy. It hunts slowly and close, pointing and retrieving both on land and "
        "in water, and it was historically used in falconry. The breed was "
        "standardised in Italy in 1950, when the club was founded to save it from "
        "extinction after the war. It is still a rare but valued gundog and a "
        "gentle family companion."
    ),
    "kai": (
        "The Kai is a medium-sized Japanese spitz from the mountains of Yamanashi "
        "Prefecture, and it takes its name from the old province of Kai. The breed "
        "has been kept there for centuries to hunt deer and wild boar in steep, "
        "snowy country. It is one of the few Japanese breeds with a brindle coat, "
        "and it is known for being independent and agile. The Kai was designated a "
        "national monument in Japan in 1934, and it remains rare outside its "
        "homeland."
    ),
    "keeshond-wolfspitz": (
        "The Keeshond, or Wolfspitz, is the largest of the German Spitz varieties "
        "and the old barge dog of the Netherlands. Bargemen kept these grey, "
        "fox-faced dogs on their boats as watchdogs and companions along the canals "
        "and rivers. The breed takes its Dutch name from Kees de Gyselaer, a "
        "eighteenth-century patriot whose dog became the emblem of a political "
        "movement. The first standard was written in 1927, and the breed is now "
        "kept mainly as a lively family companion."
    ),
    "kleiner-munsterlander": (
        "The Kleiner Münsterländer is an old versatile gundog from the Münster "
        "region of Germany, and pointing dogs of this type appear in German "
        "paintings as early as the fifteenth century. It works before the gun, "
        "points, retrieves and tracks wounded game, and it is also used for hunting "
        "with falcons. German breeders formalised two sizes in 1919, and the small "
        "Münsterländer was recognised with its own club. Today it is a popular "
        "working gundog in Europe and a steady family dog."
    ),
    "labrador-retriever": (
        "The Labrador Retriever comes not from Labrador but from Newfoundland, "
        "where small water dogs worked with fishermen and hauled nets through icy "
        "water. British visitors bought them in the early nineteenth century, and "
        "the Earl of Malmesbury and other sportsmen bred them for retrieving game "
        "on land and in water. The Kennel Club registered the breed in 1903. It "
        "has been among the most popular family dogs in the world for decades and "
        "is widely used as a guide, assistance and rescue dog."
    ),
    "nederlandse-kooikerhondje": (
        "The Nederlandse Kooikerhondje is an old Dutch spaniel-type dog used to "
        "work duck decoys, the long funnel-shaped traps of the Netherlands. The "
        "dog lured ducks along the decoy channel with its white, feathered tail, "
        "then stayed silent while the keeper closed the trap. The breed nearly died "
        "out in the twentieth century and was rebuilt from a few dogs by Baroness "
        "van Hardenbroek van Ammerstol from 1939. The Netherlands recognised it in "
        "1971, and it remains a rare but charming companion."
    ),
    "norwegian-elkhound-grey": (
        "The Norwegian Elkhound Grey is an ancient Scandinavian spitz that has been "
        "found in burial sites dating back thousands of years. Norwegian hunters "
        "used it to find and hold moose and bear at bay while barking steadily, "
        "and it also guarded farms and herded livestock. The breed was "
        "standardised in Norway in 1901, and the grey variety is the older and "
        "more common of the two. It was recognised internationally in the early "
        "twentieth century and is still prized as a hunting and family dog."
    ),
    "nova-scotia-duck-tolling-retriever": (
        "The Nova Scotia Duck Tolling Retriever was developed in the Yarmouth "
        "county of Nova Scotia, where hunters noticed that foxes playing on the "
        "shore attracted curious waterfowl. Breeders produced a reddish dog that "
        "mimicked this behaviour, romping along the bank to lure ducks within shot, "
        "then retrieving what fell. The breed was kept locally for generations and "
        "was recognised in Canada in 1945. It remains the smallest of the "
        "retrievers and the official dog of Nova Scotia."
    ),
    "old-english-sheepdog": (
        "The Old English Sheepdog comes from the west of England, where it drove "
        "cattle and sheep to market over long distances rather than herding them in "
        "the fields. Its heavy coat protected it from weather and from the bites of "
        "the animals it moved, and its tail was traditionally docked to mark a "
        "working dog. The breed was standardised in Britain in 1888 and became a "
        "favourite show dog. Its gentle, clownish nature later made it a much-loved "
        "family pet."
    ),
    "otterhound": (
        "The Otterhound is an old British scent hound, bred to hunt otters that "
        "took fish from rivers and ponds. It works in pack, hunting by scent on "
        "land and by sight in water, and its rough coat and webbed feet suit long "
        "hours in the wet. Otter hunting was banned in Britain in 1978, and the "
        "breed went into steep decline. It was recognised in Britain in 1910, but "
        "today only a few hundred dogs exist worldwide, making it one of the rarest "
        "British breeds."
    ),
    "pekingese": (
        "The Pekingese was kept for centuries in the imperial palace of China, "
        "where only royalty and the highest nobility were allowed to own one. The "
        "dogs were bred as small, lion-like companions and were carried in the "
        "sleeves of court robes. When British troops entered the Forbidden City in "
        "1860, five palace dogs were taken to Britain, and one was given to Queen "
        "Victoria. The breed was recognised in Britain in 1893 and has been a "
        "popular companion ever since."
    ),
    "pembroke-welsh-corgi": (
        "The Pembroke Welsh Corgi is a cattle dog from Pembrokeshire in Wales, "
        "where it drove cattle to pasture and market by nipping at their heels. "
        "Old Welsh legend says the dogs were a gift from the fairies, and the "
        "breed was long kept by farmers as a tough, low-set worker. The two Welsh "
        "corgi breeds were separated in 1934, and the Pembroke was recognised "
        "internationally. Queen Elizabeth II kept Pembrokes for decades, which "
        "made the breed famous around the world."
    ),
    "pomeranian": (
        "The Pomeranian takes its name from Pomerania, the region on the Baltic "
        "coast between Germany and Poland, where large white spitz dogs were kept "
        "as sheep and sledge dogs. Breeders in Europe and Britain made the dog "
        "progressively smaller and more ornamental during the nineteenth century. "
        "Queen Victoria's small Pomeranian, which she brought back from Italy, is "
        "often credited with making the miniature size fashionable. The breed was "
        "recognised in Britain in 1870 and is now one of the smallest companion "
        "dogs in the world."
    ),
    "poodle": (
        "The Poodle descends from old European water dogs, and its name comes from "
        "the German word pudel, meaning to splash in water. It worked as a "
        "retriever in Germany and, later, as a circus and companion dog in France, "
        "where it became the national breed. The characteristic lion clip was "
        "originally practical: the chest and joints were left covered to keep the "
        "dog warm in cold water. The breed was standardised in Germany in 1904 and "
        "is bred today in three sizes: standard, miniature and toy."
    ),
    "portuguese-podengo": (
        "The Portuguese Podengo is an ancient Iberian hunting breed, and dogs of "
        "this type were already described in Portugal in the Middle Ages. It is "
        "bred in three sizes — small, medium and large — and the small Podengo "
        "hunts rabbits in packs, while the large one was used for deer and wild "
        "boar. The dogs also travelled with Portuguese navigators on their "
        "voyages. The breed was standardised in Portugal in 1955 and remains a "
        "hardy working hound as well as a lively companion."
    ),
    "pug": (
        "The Pug comes from China, where short-faced, flat-nosed dogs were kept by "
        "emperors and traded along the Silk Road. Dutch and Portuguese traders "
        "brought them to Europe in the sixteenth century, and the breed became a "
        "favourite of the Dutch court — a pug is said to have warned William the "
        "Silent of a Spanish attack. In England the Pug was bred smaller in the "
        "nineteenth century and was recognised in 1885. It is now one of the "
        "best-known toy breeds in the world."
    ),
    "puli": (
        "The Puli is a Hungarian herding dog of Central Asian origin, brought to "
        "the Carpathian basin by the Magyars more than a thousand years ago. Its "
        "corded coat protects it from weather and from the teeth of the sheep it "
        "drives, and it works in a fast, bounding style. The breed was nearly lost "
        "in the twentieth century but was revived in Hungary from the 1920s. A "
        "Hungarian Puli was used for research that led to the modern training "
        "method of clicker training."
    ),
    "rat-terrier": (
        "The Rat Terrier is an American farm dog of the early twentieth century, "
        "built from terriers, feists and other small hunting dogs brought by "
        "settlers. It earned its name by clearing rats from barns and granaries, "
        "and it also worked as a squirrel and rabbit dog and as a watchdog. The "
        "breed was popular through the 1920s and 1930s and later declined, until "
        "breeders brought it back in the 1990s. It is a hardy, low-maintenance "
        "working and family dog."
    ),
    "romagna-water-dog": (
        "The Romagna Water Dog, or Lagotto Romagnolo, comes from the lowlands of "
        "Romagna in north-eastern Italy, where it was used for centuries to flush "
        "waterfowl from the marshes. When the marshes were drained in the "
        "twentieth century, the dogs were turned to a new job: hunting truffles, "
        "which they locate entirely by scent. The breed was recognised in Italy in "
        "1991 and internationally in 2005. It is the only dog breed traditionally "
        "used for truffle hunting."
    ),
    "rottweiler": (
        "The Rottweiler is descended from Roman drover dogs that guarded and moved "
        "cattle for the legions, and some of them stayed in the German town of "
        "Rottweil. There they became the butchers' dogs, driving cattle to market "
        "and pulling carts loaded with meat, with the money tied to their collars. "
        "When railways and driving bans ended that work, the breed nearly "
        "disappeared, and a club was founded in 1901 to save it. It was recognised "
        "in Germany in 1901 and grew into a world-famous police, service and "
        "guarding breed."
    ),
    "saint-bernard": (
        "The Saint Bernard takes its name from the hospice founded in the eleventh "
        "century by Bernard of Menthon high in the Swiss Alps. The monks kept large "
        "mountain dogs to guard the pass, and from the seventeenth century they "
        "used them to find travellers lost in snow. The most famous of all, Barry, "
        "is said to have saved more than forty people, and dogs are still "
        "associated with the brandy barrel of legend. The breed was standardised "
        "in Switzerland in 1884 and is the national dog of Switzerland."
    ),
    "samoyed": (
        "The Samoyed is named after the Samoyedic peoples of Siberia, who bred "
        "white, smiling spitz dogs for herding reindeer, hauling sledges and "
        "guarding the camp. The dogs lived closely with families, even sleeping in "
        "the tents, which is why the breed is unusually people-oriented. Explorers "
        "brought them out of Siberia at the end of the nineteenth century, and the "
        "first standard was written in Britain in 1909. The breed took part in "
        "several polar expeditions, including Scott's Antarctic attempt."
    ),
    "scottish-terrier": (
        "The Scottish Terrier comes from the Highlands and islands of Scotland, "
        "where several short-legged terrier types worked the cairns and burrows. "
        "Breeders separated them in the nineteenth century, and the Aberdeen "
        "Terrier became the Scottish Terrier as we know it. The first standard was "
        "published in 1880, and the breed was recognised in Britain in 1882. Its "
        "sturdy character and famous silhouette made it a symbol of Scotland and a "
        "favourite of presidents and writers."
    ),
    "shar-pei": (
        "The Shar Pei is an ancient Chinese breed from the southern province of "
        "Guangdong, where dogs with loose, wrinkled skin and a blue-black tongue "
        "were kept for hunting, herding and guarding. The breed nearly disappeared "
        "after the Chinese revolution, and in the 1970s only a small number "
        "remained in Hong Kong and Macau. Breeders rescued it with help from the "
        "Hong Kong Kennel Club, and the Shar Pei was recognised in the United "
        "States in 1991. It is now kept chiefly as a companion dog."
    ),
    "shih-tzu": (
        "The Shih Tzu was bred in the palaces of China and is often linked to "
        "Buddhist tradition, where a small lion-like dog was a symbol of "
        "protection. Court breeders crossed Tibetan dogs with Pekingese to produce "
        "the breed we know, and the dogs were kept by emperors and nobles for "
        "centuries. The breed left China in the 1920s and 1930s, when a few dogs "
        "were taken to Britain, and was recognised there in 1946. Its name means "
        "little lion."
    ),
    "siberian-husky": (
        "The Siberian Husky was bred by the Chukchi people of north-eastern "
        "Siberia to pull light sledges over enormous distances with little food. "
        "The dogs lived with the families and were valued for their endurance, "
        "friendly nature and thick double coat. They were brought to Alaska in "
        "1909 for sled racing and in 1925 famously carried diphtheria serum to "
        "Nome in a relay of teams. The breed was recognised in the United States "
        "in 1930 and is now a popular companion and sport dog."
    ),
    "sloughi": (
        "The Sloughi is a sighthound of the Maghreb, kept by Berber and Bedouin "
        "peoples in Morocco, Algeria, Tunisia and Libya. It hunts hare, gazelle "
        "and wild boar over open country and lives closely with the family, "
        "guarding the camp at night. The breed is mentioned in Arab poetry and was "
        "brought to Europe in the nineteenth century. A French club was founded in "
        "1927, and the Sloughi was recognised internationally in 1935."
    ),
    "treeing-walker-coonhound": (
        "The Treeing Walker Coonhound was developed in the United States from "
        "Virginia hounds brought west by settlers, especially the Walker dogs of "
        "Kentucky. Hunters wanted a fast, cold-nosed hound that could trail "
        "raccoon and bear and then tree them, baying in a clear, carrying voice. "
        "The breed was registered under its own name in 1945 and is one of the "
        "most popular coonhounds in America. It is still mainly a hunting dog, "
        "with a gentle temperament at home."
    ),
    "weimaraner": (
        "The Weimaraner comes from the court of Weimar in Germany, where "
        "nineteenth-century noblemen bred a versatile gundog for large game, "
        "birds and water work. German breeders kept it strictly controlled: "
        "before a puppy could be sold, it had to pass field tests and its parents "
        "had to be proven workers. The first club was founded in 1897, and the "
        "breed reached the United States in 1929. Its grey ghost colour and "
        "velvet coat made it a distinctive sporting and companion dog."
    ),
    "whippet": (
        "The Whippet comes from the north of England, where nineteenth-century "
        "miners bred a small, quiet sighthound they could keep in a small house "
        "and race on a straight track after work. It was crossed from greyhounds "
        "and terriers and was used to course rabbits, an activity called "
        "snap-dog. Racing clubs appeared in the 1890s, and the Whippet was "
        "recognised in Britain in 1891. It is the fastest dog of its size and one "
        "of the calmest indoors."
    ),
    "wire-fox-terrier": (
        "The Wire Fox Terrier is a British terrier from the fox-hunting "
        "districts of England, where its job was to bolt foxes from their earths "
        "so the hounds could continue the chase. The smooth and wire varieties "
        "were separated by breed clubs formed in 1876, and the wire became the "
        "more popular of the two. It was recognised in Britain in 1877 and soon "
        "became a leading show dog, winning more Best in Show titles than any "
        "other breed at Crufts."
    ),
    "xoloitzcuintli": (
        "The Xoloitzcuintli, or Mexican Hairless, is one of the oldest dog breeds "
        "of the Americas: hairless dogs were kept in Mexico for more than three "
        "thousand years. The Aztecs named them after the god Xolotl and believed "
        "they guided souls, and they also served as healers and companions. The "
        "breed nearly disappeared in the twentieth century and was saved by "
        "Mexican breeders from the 1950s. Mexican cynology recognised it in 1956, "
        "and it is now bred in three sizes with both hairless and coated dogs."
    ),
    "yakutian-laika": (
        "The Yakutian Laika is an ancient aboriginal breed of the Sakha Republic "
        "in Siberia, where it worked in one of the coldest inhabited places on "
        "earth. The dogs pulled sledges, hunted waterfowl and, above all, herded "
        "reindeer, living beside families in extreme cold. They were almost lost "
        "during the Soviet period, and Russian breeders began to reconstruct the "
        "breed in the 1990s. It was recognised in Russia in 2005 and "
        "internationally in 2019, and it remains rare outside Siberia."
    ),
    "yorkshire-terrier": (
        "The Yorkshire Terrier was created in the north of England in the "
        "nineteenth century, when Scottish weavers moved to Yorkshire with their "
        "small terriers. Workers crossed those dogs with local terriers to produce "
        "a tiny ratter for the mills and mines, and the breed was shown as the "
        "Broken-Haired Scotch Terrier until 1870. It was recognised in Britain in "
        "1886 and soon became a fashionable companion. Today it is one of the "
        "smallest breeds in the world and a popular lap dog."
    ),
    "brussels-griffon": (
        "The Brussels Griffon comes from Belgium, where coachmen in the "
        "nineteenth century kept small, rough-coated dogs in their stables to hunt "
        "rats and warn of strangers. The breed was built from the Griffon "
        "d'Écurie, the Belgian street dog and the small Pug, which gave it the "
        "short face and human-like expression. Two coat types developed, and the "
        "smooth one is now called the Petit Brabançon. Belgium recognised the "
        "breed in 1904, and it became known worldwide after a Griffon appeared in "
        "the film As Good as It Gets."
    ),
    # <<< END EN >>>
}

HISTORY_RU = {
    "afghan-hound": (
        "Афганская борзая — одна из древнейших борзых: изображения и записи "
        "говорят, что собаки такого типа жили в Афганистане и окрестных горах "
        "тысячи лет назад. Местные охотники травили с ними зайца и газель по "
        "каменистой пересечённой местности, где одной скорости было мало. "
        "Британские офицеры привезли породу домой в конце XIX века, а первые "
        "афганы были показаны в Британии в 1907 году. Кеннел-клуб признал породу "
        "в 1926 году, а аристократическая внешность сделала её иконой моды "
        "1960–1970-х годов."
    ),
    "airedale-terrier": (
        "Эрдельтерьер родом из долины реки Эйр в Йоркшире: в XIX веке рабочие "
        "скрестили там ныне исчезнувшего староанглийского чёрно-подпалого терьера "
        "с оттерхаундом. Целью был пёс, который гоняет выдру и крыс, работает под "
        "ружьём и при этом охраняет двор. Его назвали королём терьеров, а в "
        "Первую мировую британские солдаты использовали эрделя как связного и "
        "караульную собаку. В Британии породу признали в 1886 году, позже она "
        "распространилась как семейный компаньон и полицейская собака."
    ),
    "akita": (
        "Акиту разводят на севере Японии уже много веков, она связана с горными "
        "районами префектуры Акита, где её использовали на охоте на медведя, "
        "кабана и оленя. В японской традиции эту собаку считали символом здоровья "
        "и удачи, а её маленькие статуэтки до сих пор дарят близким. После Второй "
        "мировой войны порода почти исчезла и была восстановлена по немногим "
        "уцелевшим линиям. Самый известный акита, Хатико, почти десять лет ждал "
        "хозяина на токийской станции — ему поставили бронзовый памятник."
    ),
    "alaskan-malamute": (
        "Аляскинский маламут назван в честь инуитов-малемутов Аляски, которые "
        "держали тяжелых ездовых собак задолго до прихода европейцев. Эти псы "
        "перевозили нарты с мясом, шкурами и лагерным скарбом, а в начале XX века "
        "работали и в полярных экспедициях. Во время клондайкской золотой "
        "лихорадки породу скрещивали с более мелкими и быстрыми ездовыми "
        "собаками, и её первоначальный тип почти потерялся. В 1920–1930-е годы "
        "заводчики вернули тяжёлого, мощного маламута, и в 1935 году его признали "
        "в США."
    ),
    "american-cocker-spaniel": (
        "Американский кокер-спаниель происходит от собак, привезённых в Северную "
        "Америку из Англии в XIX веке, когда кокер ещё считался одной породой с "
        "английским кокером. Американские заводчики хотели меньшую, шелковистую "
        "собаку для охоты на вальдшнепа в густых зарослях. Типы разошлись, и в "
        "1946 году американского кокера признали самостоятельной породой. В XX "
        "веке он стал одним из самых популярных компаньонов и прообразом "
        "диснеевской Леди."
    ),
    "american-eskimo-dog": (
        "Американская эскимосская собака происходит от белых шпицев, привезённых "
        "в США немецкими иммигрантами в XIX веке. Они выступали в бродячих "
        "цирках, и благодаря их трюкам маленький белый пёс стал известен по всей "
        "стране. С ростом антинемецких настроений в Первую мировую войну имя "
        "«немецкий шпиц» сменили на «американская эскимосская собака». В 1995 "
        "году породу признали в США; её и сегодня ценят как живого семейного пса "
        "и сторожа."
    ),
    "american-staffordshire-terrier": (
        "Американский стаффордширский терьер ведёт начало от буль-энд-терьеров, "
        "привезённых в США из Британии в XIX веке. Американские заводчики сделали "
        "собаку выше и тяжелее английской и использовали её и на ферме, и в "
        "семье, и в яме. Сначала её регистрировали как американского бультерьера, "
        "затем как стаффордширского терьера. Имя «американский стаффордширский "
        "терьер» приняли в 1969 году, чтобы отделить породу от английского "
        "стаффордширского бультерьера; сегодня это популярный семейный компаньон."
    ),
    "anatolian-shepherd-dog": (
        "Анатолийская овчарка — древний сторожевой пёс плоскогорий Анатолии в "
        "Турции. Веками она жила с пастухами и их отарами, охраняя овец от волков "
        "и медведей, но не пася их. Собак отбирали по выносливости, "
        "самостоятельности и умению работать в одиночку в суровом климате. В "
        "1970-е годы в Турции начали записывать породу, и она распространилась в "
        "Европе и США как рабочий охранник и спокойная, внушительная семейная "
        "собака."
    ),
    "australian-shepherd": (
        "Австралийская овчарка была выведена на западе США, а не в Австралии, "
        "хотя её предками были баскские и австралийские пастушьи собаки. Фермерам "
        "нужен был пёс, способный перегонять овец и коров на большие расстояния и "
        "работать в жару, пыль и снег. Породу держали рабочие семьи и участники "
        "родео, а имя ей дал скот и пастухи, прибывавшие с австралийскими "
        "грузами. В 1991 году её признали в США, и сегодня это одна из самых "
        "известных пастушьих пород."
    ),
    "azawakh": (
        "Азавак — борзая Сахеля, выведенная туарегами и другими кочевыми народами "
        "Мали, Нигера и Буркина-Фасо. Она охотится на газель и зайца в открытой "
        "пустыне и охраняет лагерь, живя бок о бок с людьми. Порода названа по "
        "долине Азавак, а её сухое телосложение приспособлено к жаре и долгим "
        "переходам. Первые азаваки попали в Европу в 1970-е годы, а международное "
        "признание порода получила в 1981 году."
    ),
    "barbado-da-terceira": (
        "Барбадо да Терсейра родом с острова Терсейра в Азорском архипелаге, где "
        "её разводили для работы с крупным рогатым скотом на грубой вулканической "
        "земле. Островным фермерам нужна была собака среднего размера, которая и "
        "пасёт, и охраняет усадьбу, и ласкова с семьёй. За пределами Азор порода "
        "оставалась почти неизвестной веками, и лишь в XX веке местные заводчики "
        "спасли её. В 2004 году её признали в Португалии; сегодня это редкая, но "
        "постепенно растущая пастушья и домашняя собака."
    ),
    "basset-hound": (
        "Бассет-хаунд происходит от французских гончих, которых держали аббатства "
        "и знатные дома для охоты на кролика и оленя. Низкорослый, медлительный "
        "тип появился во Франции в XVI веке и был усовершенствован в XIX, когда "
        "охотникам понадобилась собака, за которой можно идти пешком. Британские "
        "заводчики привезли породу в 1866 году и придали ей современный облик. В "
        "1880 году её признали в Британии, а в XX веке она стала знаменитой "
        "рекламной и семейной собакой."
    ),
    "bedlington-terrier": (
        "Бедлингтон-терьер был выведен в шахтёрском краю Нортумберленда и назван "
        "по городу Бедлингтон. Шахтёры и браконьеры использовали его для охоты на "
        "крыс, кроликов и выдру, и он мог пролезать в узкие норы. Его ягнёнковая "
        "шерсть и горбатая спина скрывают крепкого терьера, а раньше породу "
        "называли ротберийским терьером. В 1877 году её признали в Британии, "
        "позже она стала выставочной и семейной собакой."
    ),
    "bichon-frise": (
        "Бишон-фризе происходит от маленьких белых собак, которых моряки и "
        "торговцы возили по Средиземноморью в Средние века. Тип был "
        "усовершенствован во Франции, где бишон стал любимцем двора, а позже — "
        "уличных артистов и шармантщиков. Его пышная курчавая шерсть и весёлый "
        "нрав сделали его популярной цирковой собакой. Во Франции породу признали "
        "в 1933 году, в США — в 1972, и сегодня это любимый компаньон."
    ),
    "black-and-tan-coonhound": (
        "Блэк-энд-тан кунхаунд был выведен в США из европейских гончих, "
        "привезённых переселенцами, в первую очередь тальботхаунда и бладхаунда. "
        "Охотникам нужна была собака, способная ночью идти по следу енота или "
        "медведя и затем облаивать зверя на дереве. Порода работает исключительно "
        "чутьём и знаменита глубоким, ровным голосом на следу. В 1945 году её "
        "признали в США, и она остаётся специализированной охотничьей собакой."
    ),
    "bloodhound": (
        "Бладхаунд — одна из древнейших гончих: его предков описывали в Европе "
        "уже в VII веке, а сам тип усовершенствовали монахи в Бельгии и Франции. "
        "Название говорит о «чистокровности» линии, а не о крови как таковой. "
        "Веками его использовали для работы по следу оленя, кабана, а позже — "
        "человека, и его результаты принимали в судах. В 1897 году породу "
        "стандартизировали в Британии, и она до сих пор остаётся эталоном "
        "розыскной работы по следу."
    ),
    "bolognese": (
        "Болоньез — маленькая белая собака-компаньон из итальянской Болоньи, и её "
        "предки встречаются на картинах эпохи Возрождения. Знатные семьи держали "
        "их как комнатных собак и дарили другим европейским дворам как "
        "дипломатический подарок. В XIX веке порода почти исчезла и была "
        "восстановлена по немногим уцелевшим линиям в XX веке. В Италии болоньеза "
        "признали в 1956 году, и за пределами родины он до сих пор редок."
    ),
    "border-collie": (
        "Бордер-колли сформировалась на границе Англии и Шотландии, где пастухам "
        "нужна была собака, управляющая отарой в горах по одному приказу или "
        "свистку. Отбор шёл на ум, выносливость и, главное, на тихий "
        "контролирующий взгляд, который стали называть «глазом». Имя "
        "«бордер-колли» закрепилось в 1915 году, до этого собак звали просто "
        "рабочими колли. Порода и сегодня считается эталоном в соревнованиях по "
        "пастьбе, а один из её представителей, Чейзер, выучил имена более тысячи "
        "игрушек."
    ),
    "border-terrier": (
        "Бордер-терьер родом с Чевиотских холмов на границе Англии и Шотландии, "
        "где он работал с фоксхаундами и охотился на лис, угрожавших овцам. Ему "
        "нужно было быть достаточно узким, чтобы идти за лисой в нору, и "
        "достаточно выносливым, чтобы целый день следовать за лошадьми. Сначала "
        "его показывали как кокетдейлского терьера, а имя «бордер» он получил в "
        "1880 году. В 1920 году породу признали в Британии; она и сейчас остаётся "
        "рабочим терьером и крепкой семейной собакой."
    ),
    "borzoi": (
        "Русскую псовую борзую создали русские дворяне, скрещивая арабских и "
        "персидских борзых с местными густошёрстными охотничьими собаками. Её "
        "использовали в охоте на волка, работая парами или небольшими стаями "
        "вместе с борзятниками на лошадях. Порода держалась почти исключительно в "
        "аристократических усадьбах, и революция 1917 года её почти уничтожила. "
        "Уцелевших собак вывезли в 1920-е годы, и в XX веке порода утвердилась "
        "как элегантная выставочная и домашняя собака."
    ),
    "boxer": (
        "Боксёр был выведен в Германии в XIX веке от булленбейсера и английского "
        "бульдога. Мюнхенские заводчики хотели получить мощного сторожа и пастуха "
        "крупного скота с короткой чистой головой и ровным характером. Первая "
        "собака была зарегистрирована в 1904 году, и порода быстро "
        "распространилась как полицейская и военная. В Первую мировую боксёр "
        "служил связным и часовым, а после войны стал одной из самых популярных "
        "семейных собак Европы и Северной Америки."
    ),
    "brussels-griffon": (
        "Брюссельский гриффон родом из Бельгии, где в XIX веке кучера держали в "
        "конюшнях небольших жесткошёрстных собак для ловли крыс и предупреждения "
        "о чужих. Породу построили на гриффоне-конюшенном, бельгийской уличной "
        "собаке и маленьком мопсе, который дал ей короткую морду и почти "
        "человеческое выражение. Сложились два типа шерсти, и гладкий теперь "
        "называется пти-брабансон. В 1904 году породу признали в Бельгии, а "
        "мировую известность ей принёс фильм «Лучше не бывает»."
    ),
    "bulldog": (
        "Английский бульдог происходит от старых английских мастифообразных "
        "собак, которых использовали в травле быков — жестоком зрелище, "
        "запрещённом в Британии в 1835 году. Когда травля закончилась, заводчики "
        "превратили собаку в добродушного компаньона и придали ей тяжёлую "
        "короткомордую форму. Первый клуб породы открылся в 1875 году, а бульдог "
        "стал символом Британии — в карикатурах его сравнивали с характером самой "
        "страны. Современное разведение сосредоточено на здоровье, дыхании и "
        "подвижности."
    ),
    "bull-terrier": (
        "Бультерьер был создан в Англии XIX века скрещиванием старого "
        "буль-энд-терьера с ныне исчезнувшим белым английским терьером. Джеймс "
        "Хинкс стремился получить полностью белую, атлетичную собаку с яйцевидной "
        "головой, и в 1887 году породу признали в Британии. Цветных собак "
        "добавили в XX веке и зарегистрировали как стаффордширских бультерьеров. "
        "Бультерьер стал известен как спортивный и армейский талисман, а позже — "
        "как стильный городской компаньон."
    ),
    "cane-corso": (
        "Кане-корсо родом из южной Италии и происходит от древних римских "
        "молоссов, которых использовали для охраны, охоты и войны. Его название "
        "восходит к латинскому слову «телохранитель»: веками пёс работал на "
        "фермах, пас скот и охранял усадьбу. После Второй мировой войны порода "
        "почти исчезла и была спасена итальянскими энтузиастами в 1970-е годы. В "
        "1987 году в Италии утвердили стандарт, и сегодня кане-корсо — популярный "
        "охранник и семейная собака по всему миру."
    ),
    "catahoula-leopard-dog": (
        "Катахула — официальная собака штата Луизиана, названная по приходу "
        "Катахула. Порода сложилась из собак испанских исследователей, "
        "французских поселенцев и индейских псов, а её крапчатый «леопардовый» "
        "окрас уникален среди рабочих пород. С её помощью пасли диких свиней и "
        "скот в болотах и сосновых лесах, работая стаями. В 1979 году породу "
        "официально признали в США, и она до сих пор остаётся прежде всего "
        "рабочей собакой."
    ),
    "cavalier-king-charles-spaniel": (
        "Кавалер-кинг-чарльз-спаниель возрождает облик маленьких комнатных "
        "спаниелей, которых писали рядом с европейской знатью в XVI–XVII веках. "
        "Карл II так любил этих собак, что тип назвали его именем. К XX веку "
        "старый облик вытеснил плоскомордый английский той-спаниель, и "
        "американские заводчики назначили приз за собак с длинной мордой, как на "
        "старых полотнах. В Британии кавалера признали в 1945 году, и с тех пор "
        "он стал одной из самых популярных пород-компаньонов."
    ),
    "collie-rough": (
        "Колли (длинношёрстный) — шотландская пастушья собака из Хайленда, где "
        "она работала с овцами в горах и в любую погоду. Породу усовершенствовали "
        "в XIX веке, а любовь королевы Виктории к этим собакам сделала их модными "
        "за пределами Шотландии. Имя происходит от старого шотландского слова, "
        "означавшего полезную чёрно-белую овчарку. В Британии породу признали в "
        "1874 году, а книги и фильмы о Лесси превратили колли во всемирный символ "
        "верного семейного пса."
    ),
    "czechoslovakian-wolfdog": (
        "Чехословацкая волчья собака появилась в 1955 году как военный "
        "эксперимент в Чехословакии: немецкую овчарку скрестили с карпатским "
        "волком. Целью было соединить обучаемость овчарки с выносливостью и "
        "чутьём волка для охраны границы. Скрещивание удалось, но собаки "
        "оказались трудны в дрессировке и в больших количествах в армии не "
        "использовались. В Чехословакии породу признали в 1982 году, на "
        "международном уровне — в 1999; сегодня её держат как требовательную "
        "рабочую и домашнюю собаку."
    ),
    "dachshund": (
        "Такса выводилась в Германии на протяжении нескольких веков из "
        "низкорослых охотничьих собак, способных идти за барсуком и лисой в нору. "
        "Название означает «барсучья собака», а в немецких записях порода "
        "встречается с XV века. Были выведены три типа шерсти и два размера для "
        "разной дичи, и собак использовали также в сворах на кабана и оленя. В "
        "1881 году её признали в Британии, и она стала любимой собакой дома — "
        "длинной, низкой и очень преданной."
    ),
    "dalmatian": (
        "Далматин назван по адриатической области Далмация, а собаки такого "
        "пятнистого типа встречаются на картинах и в церковных записях XVII–XVIII "
        "веков. Порода работала каретной собакой: бежала рядом с экипажем или под "
        "осью, разгоняла дорогу и охраняла лошадей на постоялых дворах. "
        "Британские заводчики стандартизировали её в XIX веке, и в 1888 году "
        "порода была признана. Связь с пожарными началась тогда, когда при конных "
        "пожарных обозах держали далматинов для успокоения лошадей."
    ),
    "dobermann": (
        "Доберман был создан в 1890-е годы Фридрихом Луисом Доберманом, немецким "
        "сборщиком налогов и ловчим из Апольды. Ему нужна была бесстрашная и "
        "умная собака-охранник, способная сопровождать его в опасных обходах, и "
        "он построил породу на нескольких сторожевых и охотничьих типах. Первый "
        "клуб появился в 1899 году, и собака быстро распространилась как "
        "полицейская и военная. В начале XX века породу признали на международном "
        "уровне; она и сейчас остаётся одной из самых уважаемых служебных собак."
    ),
    "drever": (
        "Древер — шведская гончая, выведенная от вестфальской таксы-бракки и "
        "других немецких охотничьих собак, привезённых на север в XIX веке. "
        "Шведским охотникам нужна была низкорослая, ровная гончая, которая идёт "
        "по следу косули и зайца по снегу и в густом лесу со скоростью пешего "
        "человека. Долго её называли шведской таксой-браккой, а имя «древер» "
        "порода получила в 1947 году. В Швеции она признана национально и "
        "остаётся одной из самых популярных охотничьих собак страны."
    ),
    "dutch-shepherd-dog": (
        "Голландская овчарка — пастушья порода Нидерландов, выведенная в трёх "
        "типах шерсти: короткой, длинной и жёсткой. Фермеры держали её, чтобы "
        "пасти овец и скот, охранять двор и возить небольшие тележки, а также "
        "использовали как полицейскую и связную собаку. В 1898 году с основанием "
        "голландского клуба породу стандартизировали, а после Второй мировой "
        "войны поголовье резко сократилось. Серьёзное разведение возобновилось в "
        "1970-е, и сегодня собаку применяют в полиции и поисковой работе."
    ),
    "english-setter": (
        "Английский сеттер формировался в Британии более четырёхсот лет из собак, "
        "которые при чутье дичи припадали к земле, позволяя охотнику накрыть птиц "
        "сетью. В XIX веке Эдвард Лаверак и Перселл Ллевеллин создали две линии, "
        "от которых происходят почти все современные сеттеры. В 1874 году породу "
        "признали в Британии. Она известна мягким нравом и крапчатым окрасом "
        "«белтон» и до сих пор работает легавой и живёт как семейная собака."
    ),
    "french-bulldog": (
        "Французский бульдог начался с маленьких английских бульдогов, которых "
        "держали кружевницы Ноттингема: в 1860-е годы они перевезли своих собак "
        "во Францию. В Париже эти псы стали любимцами общества и художников, а "
        "французские заводчики отбирали стоячие «летучие» уши и компактное тело. "
        "В 1898 году породу признали и во Франции, и в США. Пережив падение "
        "популярности в начале XX века, сегодня это одна из самых "
        "распространённых собак-компаньонов в мире."
    ),
    "german-shepherd-dog": (
        "Немецкая овчарка была основана в 1899 году Максом фон Штефаницем, "
        "который хотел получить рабочую пастушью собаку большого ума и "
        "выносливости. Он купил пса Гектора, переименовал его в Хоранда фон "
        "Графрат и вместе с клубом SV начал доказывать ценность породы на службе. "
        "Собака быстро распространилась как полицейская, военная и "
        "собака-поводырь и прославилась в обеих мировых войнах. В начале XX века "
        "породу признали на международном уровне; она остаётся одной из самых "
        "востребованных рабочих пород."
    ),
    "german-shorthaired-pointer": (
        "Курцхаар происходит из Германии XIX века, где охотнику нужна была одна "
        "собака на всё: стойка, подача, след и работа в воде. Породу построили на "
        "старых немецких легавых, гончих и водяных собаках, а развитием руководил "
        "принц Альбрехт цу Сольмс-Браунфельс. Первая родословная книга вышла в "
        "1872 году. В 1930 году породу признали в США, и сегодня это одна из "
        "самых универсальных охотничьих собак мира."
    ),
    "german-spitz": (
        "Немецкий шпиц принадлежит к древнейшему семейству собак Центральной "
        "Европы — типу шпица, который веками держали при домах и фермах. Порода "
        "делится по размеру на вольфшпица, большого, среднего, малого и "
        "померанского, и всех их объединяют стоячие уши, густая шерсть и "
        "закрученный хвост. Шпицы работали сторожами, пастухами и компаньонами, а "
        "их изображения встречаются в немецком искусстве Средневековья. В 1899 "
        "году породу стандартизировали в Германии, а в XX веке признали на "
        "международном уровне."
    ),
    "golden-retriever": (
        "Золотистый ретривер был создан в Шотландском Хайленде во второй половине "
        "XIX века Дадли Марджорибэнксом, будущим лордом Твидмутом. Он скрестил "
        "жёлтого волнистошёрстного ретривера с ныне исчезнувшим твидским водяным "
        "спаниелем, чтобы получить послушную собаку для подачи дичи с земли и из "
        "воды. Первый помёт родился в 1868 году, и линию десятилетиями держали в "
        "секрете. В Британии породу признали в 1913 году; сегодня это одна из "
        "самых любимых семейных, а также собак-поводырей и спасателей."
    ),
    "great-dane": (
        "Немецкий дог был выведен в Германии от старых мастифообразных и "
        "охотничьих собак, а современный тип закрепили в конце XIX века. Он "
        "немецкий, несмотря на английское название: породу звали «Deutsche "
        "Dogge», и в 1880 году комитет в Берлине утвердил первый стандарт. Собаку "
        "разводили для охоты на кабана с лошади и для охраны усадеб, а рост и "
        "спокойная стать принесли ей прозвище «Аполлон собачьего мира». В начале "
        "XX века породу признали на международном уровне."
    ),
    "hovawart": (
        "Ховаварт — старая немецкая фермерская собака, чьё имя означает «страж "
        "двора»; собаки этого типа упоминаются в немецких правовых кодексах "
        "Средневековья. Современную породу воссоздали в 1920-е годы заводчики, "
        "искавшие в Шварцвальде и Гарце собак, соответствующих старым описаниям. "
        "Их скрещивали с немецкими овчарками, ньюфаундлендами и леонбергерами, "
        "чтобы закрепить тип. В 1937 году ховаварта признали в Германии; его и "
        "сегодня держат в основном как рабочего охранника и семейную собаку."
    ),
    "irish-wolfhound": (
        "Ирландский волкодав — древняя ирландская борзая, с которой охотились на "
        "волка, лося и кабана; он встречается в ирландских записях и сагах с "
        "первых веков нашей эры. Ирландские вожди дарили этих собак европейским и "
        "английским королям — это и помогло породе распространиться, и позже "
        "истощило её. К XIX веку волков не осталось, и порода почти исчезла; "
        "капитан Джордж Грэм восстановил её по уцелевшим линиям и похожим борзым. "
        "В 1886 году её признали в Британии; это самая высокая порода собак."
    ),
    "italian-sighthound": (
        "Малая итальянская борзая, или левретка, — небольшая борзая, которая "
        "встречается в итальянском искусстве начиная с римской эпохи и которую "
        "держали знатные семьи по всему полуострову. С ней травили зайца и "
        "кролика, но прежде всего она была изящным компаньоном при дворах "
        "Флоренции и Милана. В 1928 году породу стандартизировали в Италии, а "
        "первые собаки попали в Британию в 1950-е годы. Её тонкое сложение и "
        "тихий нрав сделали её популярной городской собакой."
    ),
    "italian-spinone": (
        "Итальянский спиноне — жесткошёрстная легавая из Пьемонта и Ломбардии, "
        "где она веками работала в полях и на болотах северной Италии. Она ищет "
        "медленно и близко, делает стойку и подаёт дичь и на суше, и в воде, а "
        "раньше её использовали и в соколиной охоте. В 1950 году в Италии "
        "утвердили стандарт, когда клуб взялся спасать породу от исчезновения "
        "после войны. Это по-прежнему редкая, но ценимая легавая и мягкий "
        "семейный компаньон."
    ),
    "kai": (
        "Кай — японский шпиц среднего размера из гор Яманаси, названный по старой "
        "провинции Кай. Породу держат там веками для охоты на оленя и кабана в "
        "крутых снежных горах. Это одна из немногих японских пород с тигровым "
        "окрасом, и она известна самостоятельностью и ловкостью. В 1934 году кая "
        "объявили в Японии памятником природы, и за пределами родины он остаётся "
        "редким."
    ),
    "keeshond-wolfspitz": (
        "Кеесхонд, или вольфшпиц, — самый крупный из немецких шпицев и старая "
        "баржевая собака Нидерландов. Баржевники держали этих серых лисообразных "
        "псов на судах как сторожей и компаньонов на каналах и реках. Голландское "
        "имя породы идёт от Кееса де Гизелара, патриота XVIII века, чья собака "
        "стала знаком политического движения. Первый стандарт написали в 1927 "
        "году, и сегодня кеесхонда держат в основном как живого семейного "
        "компаньона."
    ),
    "kleiner-munsterlander": (
        "Кляйн-мюнстерлендер — старая универсальная легавая из района Мюнстера в "
        "Германии, а легавые этого типа встречаются на немецких полотнах уже в XV "
        "веке. Она работает перед ружьём, делает стойку, подаёт и идёт по следу "
        "подранка, а также используется в охоте с соколом. В 1919 году немецкие "
        "заводчики оформили два размера, и малый мюнстерлендер получил свой клуб. "
        "Сегодня это популярная рабочая легавая Европы и ровная семейная собака."
    ),
    "labrador-retriever": (
        "Лабрадор-ретривер происходит не из Лабрадора, а с Ньюфаундленда, где "
        "небольшие водяные собаки работали с рыбаками и тянули сети в ледяной "
        "воде. Британцы покупали их в начале XIX века, а лорд Малмсбери и другие "
        "охотники разводили их для подачи дичи на земле и в воде. В 1903 году "
        "породу зарегистрировал Кеннел-клуб. Уже десятилетия она входит в число "
        "самых популярных семейных собак мира и широко работает поводырём, "
        "ассистентом и спасателем."
    ),
    "nederlandse-kooikerhondje": (
        "Голландский койкерхондье — старая голландская собака спаниелевого типа, "
        "с которой работали на утиных «койках», длинных воронкообразных ловушках "
        "Нидерландов. Собака приманивала уток по каналу своим белым оперённым "
        "хвостом, а затем тихо ждала, пока ловчий закроет ловушку. В XX веке "
        "порода почти исчезла и была воссоздана по немногим собакам баронессой "
        "ван Харденбрук ван Аммерстол с 1939 года. В 1971 году её признали в "
        "Нидерландах; она остаётся редкой, но обаятельной собакой-компаньоном."
    ),
    "norwegian-elkhound-grey": (
        "Норвежский серый элкхаунд — древний скандинавский шпиц, останки которого "
        "находят в захоронениях возрастом в тысячи лет. Норвежские охотники "
        "использовали его, чтобы найти и облаивать лося и медведя, а также "
        "охранять дворы и пасти скот. В 1901 году в Норвегии породу "
        "стандартизировали; серый вариант — более старый и распространённый из "
        "двух. В начале XX века её признали на международном уровне, и она "
        "ценится как охотничья и семейная собака."
    ),
    "nova-scotia-duck-tolling-retriever": (
        "Новошотландский ретривер был выведен в округе Ярмут в Новой Шотландии, "
        "где охотники заметили, что играющие на берегу лисы привлекают любопытную "
        "водоплавающую птицу. Заводчики вывели рыжую собаку, имитирующую это "
        "поведение: она резвится на берегу, подманивая уток на выстрел, а затем "
        "подаёт добычу. Породу поколениями держали местные жители, а в 1945 году "
        "её признали в Канаде. Это самый маленький из ретриверов и официальная "
        "собака Новой Шотландии."
    ),
    "old-english-sheepdog": (
        "Староанглийская овчарка родом с запада Англии, где она перегоняла скот и "
        "овец на рынок на большие расстояния, а не пасла их в поле. Густая шерсть "
        "защищала её от непогоды и от зубов животных, которых она гнала, а хвост "
        "традиционно купировали в знак рабочей собаки. В 1888 году породу "
        "стандартизировали в Британии, и она стала любимицей выставок. Её добрый, "
        "шутовской нрав позже сделал её всеобщей семейной любимицей."
    ),
    "otterhound": (
        "Оттерхаунд — старая британская гончая, выведенная для охоты на выдр, "
        "которые разоряли реки и пруды. Он работает сворой, идёт по следу на "
        "земле и по зрению в воде, а грубая шерсть и перепончатые лапы помогают "
        "ему часами быть в воде. В 1978 году охоту на выдр в Британии запретили, "
        "и порода резко пошла на спад. Её признали в Британии в 1910 году, но "
        "сегодня в мире осталось лишь несколько сотен собак — это одна из самых "
        "редких британских пород."
    ),
    "pekingese": (
        "Пекинес веками жил в императорском дворце Китая, где владеть им могли "
        "только члены императорской семьи и высшая знать. Собак разводили как "
        "маленьких львиноподобных компаньонов и носили в рукавах придворных "
        "халатов. Когда в 1860 году британские войска вошли в Запретный город, "
        "пять дворцовых собак вывезли в Британию, и одну подарили королеве "
        "Виктории. В 1893 году породу признали в Британии, и с тех пор она "
        "остаётся популярным компаньоном."
    ),
    "pembroke-welsh-corgi": (
        "Вельш-корги пемброк — пастушья собака из Пембрукшира в Уэльсе, где она "
        "перегоняла скот на пастбища и рынок, покусывая его за пятки. Валлийская "
        "легенда говорит, что собак подарили людям феи, а фермеры веками держали "
        "их как крепких низкорослых работников. Две валлийские породы корги "
        "разделили в 1934 году, и пемброк получил международное признание. "
        "Королева Елизавета II десятилетиями держала пемброков, и благодаря этому "
        "порода стала известна всему миру."
    ),
    "pomeranian": (
        "Померанский шпиц назван по Померании — области на Балтийском побережье "
        "между Германией и Польшей, где держали крупных белых шпицев как овечьих "
        "и ездовых собак. В XIX веке заводчики в Европе и Британии делали собаку "
        "всё меньше и декоративнее. Маленький померанский шпиц королевы Виктории, "
        "привезённый ею из Италии, часто считается причиной моды на миниатюрный "
        "размер. В 1870 году породу признали в Британии; сегодня это одна из "
        "самых маленьких собак-компаньонов в мире."
    ),
    "poodle": (
        "Пудель происходит от старых европейских водяных собак, а его название "
        "идёт от немецкого слова pudel — «плескаться в воде». Он работал "
        "ретривером в Германии, а позже стал цирковой и комнатной собакой во "
        "Франции, где сделался национальной породой. Знаменитая «львиная» стрижка "
        "изначально была практичной: грудь и суставы оставляли одетыми, чтобы "
        "собака не мёрзла в холодной воде. В 1904 году породу стандартизировали в "
        "Германии, и сегодня её разводят в трёх размерах: большой, малый и той."
    ),
    "portuguese-podengo": (
        "Португальский поденгу — древняя иберийская охотничья порода, собаки "
        "этого типа описаны в Португалии уже в Средние века. Её разводят в трёх "
        "размерах: малый поденгу охотится на кролика в сворах, а большой "
        "использовался на оленя и кабана. Эти собаки ходили с португальскими "
        "мореплавателями в их плаваниях. В 1955 году породу стандартизировали в "
        "Португалии; она и сейчас остаётся выносливой рабочей гончей и живым "
        "компаньоном."
    ),
    "pug": (
        "Мопс родом из Китая, где короткомордых плосконосых собак держали "
        "императоры и везли по Шёлковому пути. Голландские и португальские "
        "торговцы привезли их в Европу в XVI веке, и порода стала любимицей "
        "голландского двора: говорят, мопс предупредил Вильгельма Оранского о "
        "нападении испанцев. В Англии в XIX веке мопса сделали мельче, а в 1885 "
        "году признали. Сегодня это одна из самых известных комнатных пород в "
        "мире."
    ),
    "puli": (
        "Пули — венгерская пастушья собака центральноазиатского происхождения, "
        "приведённая в Карпатский бассейн мадьярами более тысячи лет назад. Её "
        "шнуровая шерсть защищает от непогоды и от зубов овец, которых она гонит, "
        "а работает пули быстро и прыжками. В XX веке порода почти потерялась, но "
        "была восстановлена в Венгрии с 1920-х годов. Одна венгерская пули "
        "участвовала в исследованиях, которые привели к появлению современного "
        "кликер-тренинга."
    ),
    "rat-terrier": (
        "Рэт-терьер — американская фермерская собака начала XX века, собранная из "
        "терьеров, фейстов и других мелких охотничьих собак переселенцев. Имя она "
        "получила за очистку амбаров и зернохранилищ от крыс, а также работала по "
        "белке и кролику и сторожила двор. Порода была популярна в 1920–1930-е "
        "годы, затем угасла, пока заводчики не вернули её в 1990-е. Это крепкая, "
        "нетребовательная рабочая и семейная собака."
    ),
    "romagna-water-dog": (
        "Романьская водяная собака, или лаготто-романьоло, происходит из низин "
        "Романьи на северо-востоке Италии, где её веками использовали для подъёма "
        "водоплавающей птицы с болот. Когда в XX веке болота осушили, собакам "
        "нашли новую работу: поиск трюфелей, которые они находят исключительно "
        "чутьём. В Италии породу признали в 1991 году, на международном уровне — "
        "в 2005. Это единственная порода, традиционно используемая для охоты за "
        "трюфелями."
    ),
    "rottweiler": (
        "Ротвейлер происходит от римских пастушьих собак, которые охраняли и "
        "перегоняли скот для легионов, а часть их осталась в немецком городе "
        "Ротвайль. Там они стали собаками мясников: гнали скот на рынок и возили "
        "тележки с мясом, а деньги привязывали к их ошейникам. Когда железные "
        "дороги и запрет перегона скота отняли эту работу, порода почти исчезла, "
        "и в 1901 году для её спасения основали клуб. В 1901 году её признали в "
        "Германии, и она выросла в знаменитую полицейскую, служебную и охранную "
        "собаку."
    ),
    "saint-bernard": (
        "Сенбернар назван по приюту, основанному в XI веке Бернардом Ментонским "
        "высоко в Швейцарских Альпах. Монахи держали больших горных собак для "
        "охраны перевала, а с XVII века использовали их для поиска заблудившихся "
        "в снегу путников. Самый известный из них, Барри, по преданию спас более "
        "сорока человек, и с тех пор с породой связывают легендарный бочонок с "
        "бренди. В 1884 году породу стандартизировали в Швейцарии; это "
        "национальная собака страны."
    ),
    "samoyed": (
        "Самоед назван по самодийским народам Сибири, которые разводили белых "
        "улыбающихся шпицев для пастьбы оленей, перевозки нарт и охраны стойбища. "
        "Собаки жили рядом с семьями и даже спали в чумах — именно поэтому порода "
        "так ориентирована на человека. В конце XIX века их вывезли из Сибири "
        "исследователи, а первый стандарт написали в Британии в 1909 году. "
        "Самоеды участвовали в нескольких полярных экспедициях, включая попытку "
        "Скотта достичь Антарктиды."
    ),
    "scottish-terrier": (
        "Шотландский терьер родом из Хайленда и на островов Шотландии, где "
        "работало несколько низкорослых терьерных типов по каменным норам. В XIX "
        "веке их разделили, и абердинский терьер стал тем шотландским терьером, "
        "которого мы знаем. Первый стандарт опубликовали в 1880 году, а в 1882 "
        "породу признали в Британии. Крепкий характер и знаменитый силуэт сделали "
        "её символом Шотландии и любимцей президентов и писателей."
    ),
    "shar-pei": (
        "Шарпей — древняя китайская порода из южной провинции Гуандун, где собак "
        "с рыхлой морщинистой кожей и сине-чёрным языком держали для охоты, "
        "пастьбы и охраны. После китайской революции порода почти исчезла, и в "
        "1970-е годы оставалось лишь несколько собак в Гонконге и Макао. "
        "Заводчики спасли её при поддержке Гонконгского кеннел-клуба, и в 1991 "
        "году шарпея признали в США. Сегодня его держат в основном как "
        "собаку-компаньона."
    ),
    "shih-tzu": (
        "Ши-тцу разводили во дворцах Китая, и породу часто связывают с буддийской "
        "традицией, где маленький львиноподобный пёс был символом защиты. "
        "Придворные заводчики скрещивали тибетских собак с пекинесами, чтобы "
        "получить знакомый нам облик, и веками этих псов держали императоры и "
        "знать. В 1920–1930-е годы несколько собак вывезли в Британию, и в 1946 "
        "году породу там признали. Её название означает «маленький лев»."
    ),
    "siberian-husky": (
        "Сибирский хаски был выведен чукчами северо-восточной Сибири для "
        "перевозки лёгких нарт на огромные расстояния при скудном корме. Собаки "
        "жили в семьях и ценились за выносливость, дружелюбие и густой двойной "
        "мех. В 1909 году их привезли на Аляску для гонок, а в 1925 году упряжки "
        "хаски доставили в Ном противодифтерийную сыворотку. В 1930 году породу "
        "признали в США; сегодня это популярный компаньон и спортивная собака."
    ),
    "sloughi": (
        "Слуги — борзая Магриба, которую держали берберы и бедуины Марокко, "
        "Алжира, Туниса и Ливии. С ней охотились на зайца, газель и кабана в "
        "открытой местности, и она живёт рядом с семьёй, охраняя лагерь ночью. "
        "Порода упоминается в арабской поэзии и была привезена в Европу в XIX "
        "веке. Французский клуб основали в 1927 году, а международное признание "
        "слуги получил в 1935 году."
    ),
    "treeing-walker-coonhound": (
        "Триинг-уокер-кунхаунд был выведен в США от виргинских гончих, которых "
        "переселенцы привели на запад, в частности от уокеров из Кентукки. "
        "Охотникам нужна была быстрая гончая с хорошим чутьём, способная идти по "
        "следу енота или медведя и затем загонять зверя на дерево, облаивая его "
        "чистым, далеко слышным голосом. В 1945 году породу зарегистрировали под "
        "своим именем, и она стала одной из самых популярных кунхаундов Америки. "
        "Это по-прежнему прежде всего охотничья собака с мягким характером дома."
    ),
    "weimaraner": (
        "Веймаранер происходит от двора Веймара в Германии, где в XIX веке знать "
        "разводила универсальную легавую для крупного зверя, птицы и работы в "
        "воде. Немецкие заводчики держали породу под строгим контролем: прежде "
        "чем продать щенка, он должен был пройти полевые испытания, а его "
        "родители — доказать себя в работе. Первый клуб основали в 1897 году, а в "
        "1929 порода попала в США. «Серый призрак» с бархатной шерстью стал "
        "заметной охотничьей и домашней собакой."
    ),
    "whippet": (
        "Уиппет родом с севера Англии, где в XIX веке шахтёры вывели небольшую "
        "тихую борзую, которую можно держать в маленьком доме и после смены "
        "пускать по прямой дорожке. Его получили от грейхаундов и терьеров и "
        "использовали для травли кролика — это занятие называли «снэп-дог». "
        "Гоночные клубы появились в 1890-е годы, а в 1891 году породу признали в "
        "Британии. Это самая быстрая собака своего размера и одна из самых "
        "спокойных в доме."
    ),
    "wire-fox-terrier": (
        "Жесткошёрстный фокстерьер — британский терьер из областей парфорсной "
        "охоты, где его задача была выгнать лису из норы, чтобы гончие могли "
        "продолжить гон. Гладкий и жесткошёрстный варианты разделили клубы, "
        "основанные в 1876 году, и жесткошёрстный стал более популярным. В 1877 "
        "году его признали в Британии, и вскоре он стал ведущей выставочной "
        "собакой, получив больше титулов Best in Show на Crufts, чем любая другая "
        "порода."
    ),
    "xoloitzcuintli": (
        "Шолоицкуинтли, или мексиканская голая собака, — одна из древнейших пород "
        "Америки: голых собак держали в Мексике более трёх тысяч лет. Ацтеки "
        "назвали их в честь бога Шолотля и верили, что они сопровождают души, а "
        "также использовали их как целителей и компаньонов. В XX веке порода "
        "почти исчезла, но с 1950-х годов её спасли мексиканские заводчики. В "
        "1956 году её признали в Мексике, и сейчас её разводят в трёх размерах — "
        "и голых, и покрытых шерстью."
    ),
    "yakutian-laika": (
        "Якутская лайка — древняя аборигенная порода Республики Саха в Сибири, "
        "где она работала в одном из самых холодных обитаемых мест на земле. "
        "Собаки возили нарты, охотились на водоплавающую птицу и, главное, пасли "
        "оленей, живя рядом с семьями в экстремальном холоде. В советский период "
        "порода почти потерялась, и российские заводчики начали восстанавливать "
        "её в 1990-е годы. В 2005 году её признали в России, в 2019 — на "
        "международном уровне; за пределами Сибири она всё ещё редка."
    ),
    "yorkshire-terrier": (
        "Йоркширский терьер был создан на севере Англии в XIX веке, когда "
        "шотландские ткачи переехали в Йоркшир вместе со своими маленькими "
        "терьерами. Рабочие скрещивали их с местными терьерами, чтобы получить "
        "крошечного крысолова для фабрик и шахт, и до 1870 года породу показывали "
        "как жесткошёрстного шотландского терьера. В 1886 году её признали в "
        "Британии, и вскоре она стала модным компаньоном. Сегодня это одна из "
        "самых маленьких пород мира и популярная комнатная собака."
    ),
    # <<< END RU >>>
}

HISTORY_DE = {
    "afghan-hound": (
        "Der Afghane gehört zu den ältesten Windhunden: Abbildungen und Berichte "
        "zeigen, dass Hunde dieser Form schon vor Jahrtausenden in Afghanistan und "
        "den umliegenden Bergen lebten. Einheimische Jäger hetzten mit ihnen Hasen "
        "und Gazellen über steinigen, unebenen Boden, wo Geschwindigkeit allein "
        "nicht genügte. Britische Offiziere brachten die Rasse im späten 19. "
        "Jahrhundert nach Hause, und 1907 wurden die ersten Afghanen in "
        "Großbritannien ausgestellt. Der Kennel Club erkannte die Rasse 1926 an, "
        "und ihr aristokratisches Aussehen machte sie in den 1960er und 1970er "
        "Jahren zur Modeikone."
    ),
    "airedale-terrier": (
        "Der Airedale Terrier stammt aus dem Airetal in Yorkshire, wo Arbeiter im "
        "19. Jahrhundert den heute ausgestorbenen Old English Black and Tan Terrier "
        "mit dem Otterhound kreuzten. Ziel war ein Hund, der Otter und Ratten jagte, "
        "vor der Flinte arbeitete und zugleich den Hof bewachte. Er wurde als König "
        "der Terrier bekannt, und im Ersten Weltkrieg diente er als Melde- und "
        "Wachhund. 1886 wurde die Rasse in Großbritannien anerkannt und verbreitete "
        "sich später als Familien- und Polizeihund."
    ),
    "akita": (
        "Der Akita wird seit Jahrhunderten in Nordjapan gezüchtet und ist mit den "
        "Bergregionen der Präfektur Akita verbunden, wo er für die Jagd auf Bären, "
        "Wildschweine und Hirsche eingesetzt wurde. In der japanischen Tradition "
        "galt die Rasse als Symbol für Gesundheit und Glück, und kleine "
        "Statuetten werden noch heute verschenkt. Nach dem Zweiten Weltkrieg "
        "verschwand die Rasse fast und wurde aus wenigen überlebenden Linien "
        "wieder aufgebaut. Der bekannteste Akita, Hachiko, wartete fast zehn Jahre "
        "lang an einem Tokioter Bahnhof auf sein Herrchen und erhielt ein "
        "Denkmal."
    ),
    "alaskan-malamute": (
        "Der Alaskan Malamute ist nach den Mahlemut-Inuit Alaskas benannt, die "
        "lange vor der Ankunft der Europäer schwere Frachthunde hielten. Diese "
        "Hunde zogen Schlitten mit Fleisch, Häuten und Lagerausrüstung und "
        "arbeiteten Anfang des 20. Jahrhunderts auch in Polar-Expeditionen. "
        "Während des Klondike-Goldrauschs wurde die Rasse mit kleineren, "
        "schnelleren Schlittenhunden gekreuzt und verlor fast ihren ursprünglichen "
        "Typ. In den 1920er und 1930er Jahren brachten Züchter den schweren, "
        "kräftigen Malamute zurück; 1935 wurde er in den USA anerkannt."
    ),
    "american-cocker-spaniel": (
        "Der American Cocker Spaniel stammt von Hunden, die im 19. Jahrhundert aus "
        "England nach Nordamerika kamen, als der Cocker noch eine Rasse mit dem "
        "English Cocker bildete. Amerikanische Züchter wollten einen kleineren Hund "
        "mit seidigem Fell für die Waldschnepfenjagd im dichten Unterholz. Die "
        "Typen entwickelten sich auseinander, und 1946 wurde der American Cocker "
        "als eigene Rasse anerkannt. Er wurde zu einem der beliebtesten "
        "Begleithunde des 20. Jahrhunderts und zum Vorbild der Disney-Hündin Lady."
    ),
    "american-eskimo-dog": (
        "Der American Eskimo Dog stammt von weißen Spitzen ab, die deutsche "
        "Einwanderer im 19. Jahrhundert in die USA brachten. Sie traten in "
        "Wanderzirkussen auf, und durch ihre Kunststücke wurde der kleine weiße "
        "Hund landesweit bekannt. Als während des Ersten Weltkriegs die "
        "antideutsche Stimmung wuchs, wurde der Name von Deutschem Spitz in "
        "American Eskimo geändert. 1995 wurde die Rasse in den USA anerkannt; sie "
        "gilt bis heute als lebhafter Familien- und Wachhund."
    ),
    "american-staffordshire-terrier": (
        "Der American Staffordshire Terrier geht auf Bull-and-Terrier-Hunde "
        "zurück, die im 19. Jahrhundert aus England in die USA kamen. "
        "Amerikanische Züchter schufen einen größeren, schwereren Hund als das "
        "englische Original und nutzten ihn auf dem Hof, in der Familie und im "
        "Kampfring. Zuerst wurde er als American Bull Terrier registriert, später "
        "als Staffordshire Terrier. 1969 wurde der Name American Staffordshire "
        "Terrier eingeführt, um ihn vom englischen Staffordshire Bullterrier zu "
        "trennen; heute ist er ein beliebter Familienhund."
    ),
    "anatolian-shepherd-dog": (
        "Der Anatolische Hirtenhund ist ein alter Herdenschutzhund aus dem "
        "Hochland Anatoliens in der Türkei. Jahrhunderte lang lebte er mit Hirten "
        "und ihren Herden und bewachte die Schafe vor Wölfen und Bären, ohne sie "
        "zu treiben. Gezüchtet wurde er auf Ausdauer, Selbstständigkeit und die "
        "Fähigkeit, in rauem Klima allein zu arbeiten. In den 1970er Jahren begann "
        "die Türkei, die Rasse zu erfassen, und sie verbreitete sich in Europa und "
        "den USA als Arbeits- und ruhiger Familienhund."
    ),
    "australian-shepherd": (
        "Der Australian Shepherd wurde im Westen der USA entwickelt, nicht in "
        "Australien, obwohl seine Vorfahren baskische und australische Hütehunde "
        "waren. Rancher brauchten einen Hund, der Schafe und Rinder über weite "
        "Strecken trieb und in Hitze, Staub und Schnee arbeitete. Die Rasse wurde "
        "von Arbeitsfamilien und Rodeo-Reitern gehalten, und ihren Namen erhielt "
        "sie von den Schafen und Hirten, die mit australischen Schiffen kamen. "
        "1991 wurde sie in den USA anerkannt und ist heute eine der bekanntesten "
        "Hütehunderassen."
    ),
    "azawakh": (
        "Der Azawakh ist ein Windhund des Sahel, gezüchtet von den Tuareg und "
        "anderen Nomadenvölkern in Mali, Niger und Burkina Faso. Er jagt Gazellen "
        "und Hasen in der offenen Wüste und bewacht das Lager, wobei er eng mit "
        "den Menschen lebt. Die Rasse ist nach dem Azawakh-Tal benannt, und ihr "
        "schlanker Körper ist an Hitze und weite Wege angepasst. Die ersten "
        "Azawakhs kamen in den 1970er Jahren nach Europa, 1981 wurde die Rasse "
        "international anerkannt."
    ),
    "barbado-da-terceira": (
        "Der Barbado da Terceira stammt von der Azoreninsel Terceira, wo er für "
        "die Arbeit mit Rindern auf rauem Vulkangrund gezüchtet wurde. Die Bauern "
        "brauchten einen mittelgroßen Hund, der hütet, den Hof bewacht und "
        "freundlich zur Familie ist. Außerhalb der Azoren blieb die Rasse "
        "jahrhundertelang fast unbekannt und wurde im 20. Jahrhundert von "
        "einheimischen Züchtern gerettet. 2004 wurde sie in Portugal anerkannt; "
        "heute ist sie ein seltener, aber stetig wachsender Hüte- und "
        "Begleithund."
    ),
    "basset-hound": (
        "Der Basset Hound stammt von französischen Spürhunden ab, die in Klöstern "
        "und Adelshöfen zur Hasen- und Rotwildjagd gehalten wurden. Der "
        "niedrige, langsame Typ erschien im 16. Jahrhundert in Frankreich und "
        "wurde im 19. Jahrhundert verfeinert, als Jäger einen Hund wollten, dem "
        "sie zu Fuß folgen konnten. Britische Züchter importierten die Rasse 1866 "
        "und gaben ihr ihr heutiges Aussehen. 1880 wurde sie in Großbritannien "
        "anerkannt und im 20. Jahrhundert zum berühmten Werbe- und Familienhund."
    ),
    "bedlington-terrier": (
        "Der Bedlington Terrier entstand im Bergbaugebiet "
        "Northumberlands und ist nach der Stadt Bedlington benannt. Bergleute "
        "und Wilderer nutzten ihn für die Jagd auf Ratten, Kaninchen und Otter, "
        "und er konnte durch enge Baue kriechen. Sein lammartiges Fell und der "
        "gewölbte Rücken verbergen einen zähen Terrier; früher hieß er Rothbury "
        "Terrier. 1877 wurde er in Großbritannien anerkannt und später zum "
        "Ausstellungs- und Familienhund."
    ),
    "bichon-frise": (
        "Der Bichon Frisé stammt von kleinen weißen Hunden ab, die Seeleute und "
        "Händler im Mittelalter durch das Mittelmeer trugen. Der Typ wurde in "
        "Frankreich verfeinert, wo der Bichon zum Liebling des Hofes und später "
        "der Straßenkünstler und Leierkastenmänner wurde. Sein lockiges Fell und "
        "sein fröhliches Wesen machten ihn zum beliebten Zirkushund. 1933 wurde "
        "die Rasse in Frankreich anerkannt, 1972 in den USA; heute ist er ein "
        "vielgeliebter Begleiter."
    ),
    "black-and-tan-coonhound": (
        "Der Black and Tan Coonhound wurde in den USA aus europäischen "
        "Spürhunden entwickelt, die Siedler mitbrachten, vor allem aus dem Talbot "
        "und dem Bloodhound. Jäger brauchten einen Hund, der nachts die Fährte "
        "von Waschbär und Bär halten und das Tier dann verbellen konnte. Die "
        "Rasse arbeitet ausschließlich mit der Nase und ist für ihre tiefe, "
        "ruhige Stimme auf der Fährte bekannt. 1945 wurde sie in den USA "
        "anerkannt und ist bis heute ein spezialisierter Jagdhund."
    ),
    "bloodhound": (
        "Der Bloodhound ist einer der ältesten Spürhunde: Seine Vorfahren wurden "
        "in Europa bereits im 7. Jahrhundert beschrieben und von Mönchen in "
        "Belgien und Frankreich verfeinert. Der Name bezieht sich auf "
        "reinblütige, edle Zucht und nicht auf Blut. Jahrhundertelang wurde er "
        "zur Fährtenarbeit auf Rotwild, Schwarzwild und später Menschen "
        "eingesetzt, und seine Ergebnisse wurden vor Gericht anerkannt. 1897 "
        "wurde die Rasse in Großbritannien standardisiert und gilt bis heute als "
        "Maßstab für die Fährtenarbeit."
    ),
    "bolognese": (
        "Der Bologneser ist ein kleiner weißer Begleithund aus Bologna in "
        "Italien, dessen Vorfahren in der Kunst der Renaissance zu sehen sind. "
        "Adelsfamilien hielten sie als Schoßhunde und schenkten sie anderen "
        "europäischen Höfen als diplomatische Gabe. Im 19. Jahrhundert "
        "verschwand die Rasse fast und wurde im 20. Jahrhundert aus wenigen "
        "überlebenden Linien neu aufgebaut. 1956 wurde der Bologneser in Italien "
        "anerkannt, außerhalb seiner Heimat ist er bis heute selten."
    ),
    "border-collie": (
        "Der Border Collie entstand an der Grenze zwischen England und "
        "Schottland, wo Hirten einen Hund brauchten, der Schafe im Hügelland auf "
        "ein Wort oder einen Pfiff lenkt. Gezüchtet wurde auf Intelligenz, "
        "Ausdauer und vor allem auf den stillen, kontrollierenden Blick, der "
        "Eye genannt wird. Der Name setzte sich 1915 durch; zuvor hießen die "
        "Hunde einfach Working Collies. Die Rasse gilt noch heute als Maßstab im "
        "Hütehunde-Sport, und einer ihrer Vertreter, Chaser, lernte die Namen von "
        "über tausend Spielzeugen."
    ),
    "border-terrier": (
        "Der Border Terrier stammt aus den Cheviot Hills zwischen England und "
        "Schottland, wo er mit Foxhounds arbeitete und Füchse jagte, die den "
        "Schafen gefährlich wurden. Er musste schmal genug sein, um einem Fuchs in "
        "den Bau zu folgen, und zäh genug, um den ganzen Tag mit den Pferden zu "
        "laufen. Zuerst wurde er als Coquetdale Terrier ausgestellt und erhielt "
        "1880 den Namen Border. 1920 wurde er in Großbritannien anerkannt und "
        "ist bis heute Arbeits- und robuster Familienhund."
    ),
    "borzoi": (
        "Der Barsoi, der Russische Windhund, wurde von russischen Adligen aus "
        "arabischen und persischen Windhunden und einheimischen, dicht "
        "behaarten Jagdhunden geschaffen. Er wurde zur Wolfsjagd eingesetzt, "
        "arbeitete paarweise oder in kleinen Meuten und jagte zusammen mit "
        "berittenen Jägern. Die Rasse wurde fast ausschließlich vom Adel "
        "gehalten, und die Revolution von 1917 hätte sie beinahe beendet. "
        "Überlebende Hunde wurden in den 1920er Jahren exportiert, und im 20. "
        "Jahrhundert wurde der Barsoi zum eleganten Ausstellungs- und "
        "Begleithund."
    ),
    "boxer": (
        "Der Boxer wurde im 19. Jahrhundert in Deutschland aus dem Bullenbeißer "
        "und der Englischen Bulldogge entwickelt. Münchner Züchter wollten einen "
        "kräftigen Wach- und Treibhund mit kurzem, klarem Kopf und ruhigem "
        "Wesen. Der erste Boxer wurde 1904 eingetragen, und die Rasse "
        "verbreitete sich schnell als Polizei- und Militärhund. Im Ersten "
        "Weltkrieg diente der Boxer als Melde- und Wachhund, nach dem Krieg "
        "wurde er zu einem der beliebtesten Familienhunde Europas und "
        "Nordamerikas."
    ),
    "bulldog": (
        "Die Englische Bulldogge stammt von alten englischen Mastiff-Typen ab, die "
        "für das Bullenbeißen eingesetzt wurden, einen grausamen Sport, der 1835 "
        "in Großbritannien verboten wurde. Als der Sport endete, machten Züchter "
        "aus dem Hund einen gutmütigen Begleiter und gaben ihm die schwere, "
        "kurzgesichtige Form von heute. Der erste Rasseclub entstand 1875, und "
        "die Bulldogge wurde zum Nationalsymbol Großbritanniens — in Karikaturen "
        "verkörperte sie den Charakter des Landes. Die moderne Zucht legt Wert auf "
        "Gesundheit, Atmung und Beweglichkeit."
    ),
    "bull-terrier": (
        "Der Bullterrier entstand im England des 19. Jahrhunderts aus der Kreuzung "
        "des alten Bull-and-Terriers mit dem heute ausgestorbenen White English "
        "Terrier. James Hinks wollte einen rein weißen, athletischen Hund mit "
        "eiförmigem Kopf, und 1887 wurde die Rasse in Großbritannien anerkannt. "
        "Farbige Hunde kamen im 20. Jahrhundert dazu und wurden als "
        "Staffordshire Bullterrier eingetragen. Der Bullterrier wurde als Sport- "
        "und Armeemaskottchen bekannt und später als stilvoller städtischer "
        "Begleiter."
    ),
    "cane-corso": (
        "Der Cane Corso stammt aus Süditalien und geht auf die alten römischen "
        "Molosser zurück, die zum Bewachen, Jagen und im Krieg dienten. Sein Name "
        "geht auf das lateinische Wort für Leibwächter zurück, und jahrhundertelang "
        "arbeitete er auf Bauernhöfen, trieb Vieh und bewachte Anwesen. Nach dem "
        "Zweiten Weltkrieg verschwand die Rasse fast und wurde in den 1970er "
        "Jahren von italienischen Liebhabern gerettet. 1987 wurde in Italien ein "
        "Standard verfasst, und heute ist der Cane Corso ein beliebter Wach- und "
        "Familienhund."
    ),
    "catahoula-leopard-dog": (
        "Der Catahoula Leopard Dog ist der Staatshund von Louisiana und nach dem "
        "Catahoula Parish benannt. Er entstand aus Hunden spanischer Entdecker, "
        "französischer Siedler und indianischer Vorfahren, und sein geflecktes, "
        "leopardenartiges Fell ist unter Arbeitsrassen einzigartig. Mit ihm "
        "wurden wilde Schweine und Rinder in Sümpfen und Kiefernwäldern gehuetet, "
        "oft in Meuten. 1979 wurde die Rasse in den USA offiziell anerkannt und "
        "ist bis heute vor allem ein Arbeitshund."
    ),
    "cavalier-king-charles-spaniel": (
        "Der Cavalier King Charles Spaniel belebt die kleinen Spielspaniels "
        "wieder, die im 16. und 17. Jahrhundert neben dem europäischen Adel "
        "gemalt wurden. König Karl II. liebte sie so sehr, dass der Typ nach ihm "
        "benannt wurde. Im 20. Jahrhundert hatte der kurzgesichtige English Toy "
        "Spaniel das alte Aussehen verdrängt, und amerikanische Züchter stifteten "
        "einen Preis für Hunde mit der langen Schnauze der alten Gemälde. 1945 "
        "wurde der Cavalier in Großbritannien anerkannt und ist seither eine der "
        "beliebtesten Begleithunderassen."
    ),
    "collie-rough": (
        "Der Langhaarige Collie ist ein schottischer Hütehund aus dem Hochland, "
        "wo er bei jedem Wetter mit Schafen arbeitete. Die Rasse wurde im 19. "
        "Jahrhundert verfeinert, und Königin Victorias Vorliebe für diese Hunde "
        "machte sie über Schottland hinaus Mode. Der Name stammt vom alten "
        "schottischen Wort für einen nützlichen schwarz-weißen Schäferhund. 1874 "
        "wurde die Rasse in Großbritannien anerkannt, und die Romane und Filme um "
        "Lassie machten den Collie zum weltweiten Sinnbild des treuen "
        "Familienhundes."
    ),
    "czechoslovakian-wolfdog": (
        "Der Tschechoslowakische Wolfshund entstand 1955 als militärisches "
        "Experiment in der Tschechoslowakei, bei dem Deutscher Schäferhund und "
        "Karpatenwolf gekreuzt wurden. Ziel war es, die Lernfähigkeit des "
        "Schäferhundes mit Ausdauer und Sinnen des Wolfs für den Grenzdienst zu "
        "verbinden. Die Kreuzung gelang, doch die Hunde erwiesen sich als schwer "
        "auszubilden und wurden von der Armee nie in großen Zahlen genutzt. 1982 "
        "wurde die Rasse in der Tschechoslowakei anerkannt, 1999 international; "
        "heute gilt sie als anspruchsvoller Arbeits- und Begleithund."
    ),
    "dachshund": (
        "Der Dackel wurde in Deutschland über mehrere Jahrhunderte aus "
        "niedrigen Jagdhunden entwickelt, die Dachse und Füchse in ihre Baue "
        "verfolgen konnten. Der Name bedeutet Dachshund, und in deutschen "
        "Aufzeichnungen erscheint die Rasse ab dem 15. Jahrhundert. Drei "
        "Fellarten und zwei Größen wurden für unterschiedliches Wild gezüchtet, "
        "und die Hunde arbeiteten auch in Meuten auf Schwarzwild und Rotwild. "
        "1881 wurde die Rasse in Großbritannien anerkannt und zum beliebten "
        "Familienhund — lang, niedrig und sehr anhänglich."
    ),
    "dalmatian": (
        "Der Dalmatiner ist nach der adriatischen Region Dalmatien benannt, und "
        "Hunde dieses gefleckten Typs erscheinen seit dem 17. und 18. Jahrhundert "
        "in Gemälden und Kirchenbüchern. Die Rasse wurde als Kutschenhund "
        "eingesetzt: Sie lief neben oder unter der Achse, machte den Weg frei und "
        "bewachte die Pferde an den Gasthöfen. Britische Züchter standardisierten "
        "sie im 19. Jahrhundert, 1888 erfolgte die Anerkennung. Die Verbindung "
        "zur Feuerwehr begann, als bei Pferdefuhrwerken Dalmatiner gehalten "
        "wurden, um die Pferde zu beruhigen."
    ),
    "dobermann": (
        "Der Dobermann wurde in den 1890er Jahren von Karl Friedrich Louis "
        "Dobermann geschaffen, einem deutschen Steuereintreiber und Hundefänger "
        "aus Apolda. Er brauchte einen furchtlosen, klugen Wachhund für gefährliche "
        "Rundgänge und baute die Rasse aus mehreren Wach- und Jagdtypen auf. Der "
        "erste Club entstand 1899, und der Hund verbreitete sich schnell als "
        "Polizei- und Militärhund. Anfang des 20. Jahrhunderts wurde er "
        "international anerkannt und gilt bis heute als einer der angesehensten "
        "Schutz- und Diensthunde."
    ),
    "drever": (
        "Der Drever ist ein schwedischer Spürhund, der aus der Westfälischen "
        "Dachsbracke und anderen deutschen Jagdhunden entstand, die im 19. "
        "Jahrhundert in den Norden kamen. Schwedische Jäger wollten einen "
        "niedrigen, ruhigen Hund, der Reh und Hase durch Schnee und dichten Wald "
        "in einem Tempo verfolgt, dem ein Mensch folgen kann. Lange hieß er "
        "Schwedische Dachsbracke, 1947 wurde er in Drever umbenannt. In Schweden "
        "ist er national anerkannt und zählt zu den beliebtesten Jagdhunden des "
        "Landes."
    ),
    "dutch-shepherd-dog": (
        "Der Holländische Schäferhund ist die Hütehunderasse der Niederlande und "
        "wird in drei Fellarten gezüchtet: kurz, lang und rauhaarig. Bauern "
        "hielten sie, um Schafe und Vieh zu treiben, den Hof zu bewachen und "
        "kleine Wagen zu ziehen; außerdem dienten sie als Polizei- und "
        "Meldehunde. 1898 wurde die Rasse mit der Gründung des niederländischen "
        "Clubs standardisiert, und nach dem Zweiten Weltkrieg gingen die "
        "Bestände stark zurück. In den 1970er Jahren begann die Zucht neu, und "
        "heute arbeitet die Rasse bei Polizei und Suche."
    ),
    "english-setter": (
        "Der English Setter wurde über vierhundert Jahre in Großbritannien aus "
        "Vorstehhunden entwickelt, die sich bei Wild niederlegten, damit der "
        "Jäger ein Netz darüber werfen konnte. Im 19. Jahrhundert formten Edward "
        "Laverack und Purcell Llewellin die beiden Linien, von denen fast alle "
        "modernen Setter abstammen. 1874 wurde die Rasse in Großbritannien "
        "anerkannt. Sie ist für ihr sanftes Wesen und das gefleckte Belton-Fell "
        "bekannt und arbeitet noch heute als Vorstehhund und Familienbegleiter."
    ),
    "french-bulldog": (
        "Die Französische Bulldogge begann als kleine englische Bulldogge, die "
        "Spitzenklöpplerinnen in Nottingham hielten und in den 1860er Jahren mit "
        "nach Frankreich nahmen. In Paris wurden die Hunde zu Favoriten der "
        "Gesellschaft und der Künstler, und französische Züchter selektierten auf "
        "die aufrechten Fledermausohren und den kompakten Körper. 1898 wurde die "
        "Rasse in Frankreich und in den USA anerkannt. Nach einem "
        "Beliebtheitstief Anfang des 20. Jahrhunderts ist sie heute eine der "
        "häufigsten Begleithunderassen der Welt."
    ),
    "german-shepherd-dog": (
        "Der Deutsche Schäferhund wurde 1899 von Max von Stephanitz begründet, "
        "der einen Arbeits- und Hütehund von großer Intelligenz und Ausdauer "
        "wollte. Er kaufte den Hund Hektor, benannte ihn in Horand von Grafrath "
        "um und bewies mit dem Verein SV den Wert der Rasse im Dienst. Der Hund "
        "verbreitete sich schnell als Polizei-, Militär- und Blindenhund und "
        "wurde in beiden Weltkriegen berühmt. Anfang des 20. Jahrhunderts wurde "
        "die Rasse international anerkannt und zählt bis heute zu den meist "
        "genutzten Arbeitsrassen."
    ),
    "german-shorthaired-pointer": (
        "Der Deutsch Kurzhaar stammt aus dem Deutschland des 19. Jahrhunderts, "
        "wo Jäger einen Hund für alles brauchten: Vorstehen, Apportieren, "
        "Fährtenarbeit und Wasserarbeit. Die Rasse entstand aus alten deutschen "
        "Vorstehhunden, Laufhunden und Wasserhunden, und Prinz Albrecht zu "
        "Solms-Braunfels begleitete ihre Entwicklung. Das erste Zuchtbuch "
        "erschien 1872. 1930 wurde die Rasse in den USA anerkannt und ist heute "
        "einer der vielseitigsten Jagdhunde der Welt."
    ),
    "german-spitz": (
        "Der Deutsche Spitz gehört zur ältesten Hundefamilie Mitteleuropas, dem "
        "Spitztyp, der jahrhundertelang an Höfen und Häusern gehalten wurde. Die "
        "Rasse wird nach Größe in Wolfsspitz, Groß-, Mittel- und Kleinspitz sowie "
        "Pomeranian geteilt; alle haben Stehohren, dichtes Fell und die geringelte "
        "Rute. Spitze arbeiteten als Wach-, Hüte- und Begleithunde, und ihr Bild "
        "erscheint in der deutschen Kunst des Mittelalters. 1899 wurde die Rasse "
        "in Deutschland standardisiert und im 20. Jahrhundert international "
        "anerkannt."
    ),
    "golden-retriever": (
        "Der Golden Retriever wurde in der zweiten Hälfte des 19. Jahrhunderts "
        "von Dudley Marjoribanks, dem späteren Lord Tweedmouth, im schottischen "
        "Hochland geschaffen. Er kreuzte einen gelben, welligen Retriever mit dem "
        "heute ausgestorbenen Tweed Water Spaniel, um einen folgsamen Hund für "
        "die Apportierarbeit zu Land und zu Wasser zu erhalten. Der erste Wurf "
        "wurde 1868 geboren, und die Linie blieb jahrzehntelang privat. 1913 "
        "wurde die Rasse in Großbritannien anerkannt; heute gehört sie zu den "
        "beliebtesten Familien-, Blinden- und Rettungshunden."
    ),
    "great-dane": (
        "Die Deutsche Dogge wurde in Deutschland aus alten Mastiff- und "
        "Jagdhunden entwickelt, und deutsche Züchter legten im späten 19. "
        "Jahrhundert den modernen Typ fest. Die Rasse ist trotz des englischen "
        "Namens deutsch: Sie hieß Deutsche Dogge, und 1880 verabschiedete ein "
        "Komitee in Berlin den ersten Standard. Der Hund wurde für die "
        "Sauenjagd zu Pferd und zum Bewachen von Gutshöfen gezüchtet, und Größe "
        "und ruhige Haltung brachten ihm den Beinamen Apoll unter den Hunden "
        "ein. Anfang des 20. Jahrhunderts wurde die Rasse international "
        "anerkannt."
    ),
    "hovawart": (
        "Der Hovawart ist ein alter deutscher Hofhund, dessen Name Hofwart "
        "bedeutet; Hunde dieses Typs werden in deutschen Rechtsquellen des "
        "Mittelalters erwähnt. Die moderne Rasse wurde in den 1920er Jahren von "
        "Züchtern wieder aufgebaut, die im Schwarzwald und Harz nach Hunden "
        "suchten, die den alten Beschreibungen entsprachen. Sie wurden mit "
        "Deutschen Schäferhunden, Neufundländern und Leonbergern gekreuzt, um "
        "den Typ zu festigen. 1937 wurde der Hovawart in Deutschland anerkannt; "
        "er wird bis heute vor allem als Wach- und Familienhund gehalten."
    ),
    "irish-wolfhound": (
        "Der Irische Wolfshund ist ein alter irischer Windhund, mit dem Wölfe, "
        "Elche und Wildschweine gejagt wurden; er erscheint seit den ersten "
        "Jahrhunderten n. Chr. in irischen Aufzeichnungen und Sagen. Irische "
        "Häuptlinge schenkten die Hunde europäischen und englischen Königen, was "
        "die Rasse einerseits verbreitete und andererseits ausdünnte. Im 19. "
        "Jahrhundert waren die Wölfe verschwunden und die Rasse fast erloschen; "
        "Captain George Graham baute sie aus überlebenden Linien und ähnlichen "
        "Windhunden wieder auf. 1886 wurde sie in Großbritannien anerkannt; sie "
        "ist die größte aller Hunderassen."
    ),
    "italian-sighthound": (
        "Das Italienische Windspiel ist ein kleiner Windhund, der seit der "
        "römischen Zeit in der italienischen Kunst erscheint und von "
        "Adelsfamilien auf der ganzen Halbinsel gehalten wurde. Mit ihm wurden "
        "Hasen und Kaninchen gehetzt, vor allem aber war es ein eleganter "
        "Begleiter an den Höfen von Florenz und Mailand. 1928 wurde die Rasse in "
        "Italien standardisiert, und in den 1950er Jahren kamen die ersten Hunde "
        "nach Großbritannien. Sein feiner Körperbau und sein ruhiges Wesen machen "
        "es heute zu einem beliebten Stadthund."
    ),
    "italian-spinone": (
        "Der Italienische Spinone ist ein rauhaariger Vorstehhund aus Piemont "
        "und der Lombardei, der jahrhundertelang in den Feldern und Sümpfen "
        "Norditaliens arbeitete. Er sucht langsam und nah, steht vor und "
        "apportiert zu Lande und im Wasser; früher wurde er auch in der "
        "Beizjagd eingesetzt. 1950 wurde in Italien der Standard verabschiedet, "
        "als der Club die Rasse nach dem Krieg vor dem Aussterben bewahrte. Sie "
        "ist bis heute ein seltener, aber geschätzter Jagd- und sanfter "
        "Familienhund."
    ),
    "kai": (
        "Der Kai ist ein mittelgroßer japanischer Spitz aus den Bergen der "
        "Präfektur Yamanashi und trägt den Namen der alten Provinz Kai. Dort wird "
        "er seit Jahrhunderten für die Jagd auf Hirsche und Wildschweine in "
        "steilem, schneereichem Gelände gehalten. Er ist eine der wenigen "
        "japanischen Rassen mit gestromtem Fell und bekannt für seine "
        "Selbstständigkeit und Wendigkeit. 1934 wurde der Kai in Japan zum "
        "Naturdenkmal erklärt; außerhalb seiner Heimat ist er selten."
    ),
    "keeshond-wolfspitz": (
        "Der Keeshond oder Wolfsspitz ist die größte deutsche Spitzvarietät und "
        "der alte Bootshund der Niederlande. Schiffer hielten diese grauen, "
        "fuchsgesichtigen Hunde auf ihren Booten als Wächter und Begleiter auf "
        "Kanälen und Flüssen. Der niederländische Name geht auf Kees de "
        "Gyselaer zurück, einen Patrioten des 18. Jahrhunderts, dessen Hund zum "
        "Zeichen einer politischen Bewegung wurde. Der erste Standard wurde 1927 "
        "geschrieben, und heute wird der Keeshond vor allem als lebhafter "
        "Familienhund gehalten."
    ),
    "kleiner-munsterlander": (
        "Der Kleine Münsterländer ist ein alter vielseitiger Vorstehhund aus der "
        "Region Münster, und Vorstehhunde dieses Typs erscheinen schon im 15. "
        "Jahrhundert auf deutschen Gemälden. Er arbeitet vor der Flinte, steht "
        "vor, apportiert und arbeitet auf der Schweißfährte; außerdem wird er in "
        "der Beizjagd eingesetzt. 1919 legten deutsche Züchter zwei Größen fest, "
        "und der kleine Münsterländer erhielt einen eigenen Club. Heute ist er "
        "ein beliebter Arbeitshund in Europa und ein ausgeglichener "
        "Familienhund."
    ),
    "labrador-retriever": (
        "Der Labrador Retriever stammt nicht aus Labrador, sondern aus "
        "Neufundland, wo kleine Wasserhunde mit Fischern arbeiteten und Netze "
        "durch eisiges Wasser zogen. Britische Besucher kauften sie Anfang des "
        "19. Jahrhunderts, und Lord Malmesbury sowie andere Sportsmänner "
        "züchteten sie für die Apportierarbeit zu Land und zu Wasser. 1903 "
        "registrierte der Kennel Club die Rasse. Seit Jahrzehnten zählt sie zu "
        "den beliebtesten Familienhunden der Welt und arbeitet weit verbreitet "
        "als Blinden-, Assistenz- und Rettungshund."
    ),
    "nederlandse-kooikerhondje": (
        "Der Nederlandse Kooikerhondje ist ein alter spanielartiger Hund aus den "
        "Niederlanden, der an den Entenkojen arbeitete, den langen trichterförmigen "
        "Fanganlagen. Der Hund lockte Enten mit seiner weißen, gefiederten Rute "
        "den Koigraben entlang und blieb still, während der Fänger die Anlage "
        "schloss. Im 20. Jahrhundert wäre die Rasse fast verschwunden und wurde "
        "ab 1939 von Baronin van Hardenbroek van Ammerstol aus wenigen Hunden "
        "wieder aufgebaut. 1971 wurde sie in den Niederlanden anerkannt; sie "
        "bleibt selten, aber charmant."
    ),
    "norwegian-elkhound-grey": (
        "Der Norwegische Elchhund Grau ist ein alter skandinavischer Spitz, der "
        "in Grabstätten gefunden wurde, die Jahrtausende alt sind. Norwegische "
        "Jäger nutzten ihn, um Elche und Bären zu finden und durch anhaltendes "
        "Bellen zu stellen; außerdem bewachte er Höfe und hütete Vieh. 1901 "
        "wurde die Rasse in Norwegen standardisiert, und die graue Varietät ist "
        "die ältere und häufigere der beiden. Anfang des 20. Jahrhunderts wurde "
        "sie international anerkannt und gilt bis heute als Jagd- und "
        "Familienhund."
    ),
    "nova-scotia-duck-tolling-retriever": (
        "Der Nova Scotia Duck Tolling Retriever entstand im Yarmouth County in "
        "Neuschottland, wo Jäger bemerkten, dass spielende Füchse am Ufer "
        "neugieriges Wassergeflügel anlockten. Züchter schufen einen roten Hund, "
        "der dieses Verhalten nachahmt: Er tollt am Ufer und lockt Enten in "
        "Schussweite, um dann die Beute zu apportieren. Die Rasse wurde "
        "Generationen lang lokal gehalten und 1945 in Kanada anerkannt. Sie ist "
        "der kleinste Retriever und der offizielle Hund von Neuschottland."
    ),
    "old-english-sheepdog": (
        "Der Old English Sheepdog stammt aus dem Westen Englands, wo er Vieh "
        "und Schafe über weite Wege zum Markt trieb, statt sie auf der Weide zu "
        "hüten. Sein dichtes Fell schützte ihn vor Wetter und vor den Bissen der "
        "Tiere, die er trieb, und die Rute wurde traditionell kupiert, um den "
        "Arbeitshund zu kennzeichnen. 1888 wurde die Rasse in Großbritannien "
        "standardisiert und wurde zum beliebten Ausstellungshund. Sein sanftes, "
        "clownhaftes Wesen machte ihn später zum Familienliebling."
    ),
    "otterhound": (
        "Der Otterhound ist ein alter britischer Spürhund, der für die Jagd auf "
        "Fischotter gezüchtet wurde, die Flüsse und Teiche leerten. Er arbeitet "
        "in der Meute, jagt mit der Nase an Land und mit den Augen im Wasser, und "
        "sein raues Fell und die Schwimmhäute passen zu langen Stunden im "
        "Nassen. 1978 wurde die Otterjagd in Großbritannien verboten, und die "
        "Rasse ging stark zurück. 1910 wurde sie in Großbritannien anerkannt, "
        "doch heute gibt es weltweit nur wenige hundert Hunde — sie gehört zu "
        "den seltensten britischen Rassen."
    ),
    "pekingese": (
        "Der Pekinese wurde jahrhundertelang im Kaiserpalast Chinas gehalten, wo "
        "nur die kaiserliche Familie und der Hochadel einen besitzen durften. Die "
        "Hunde wurden als kleine, löwenähnliche Begleiter gezüchtet und in den "
        "Ärmeln der Hofgewänder getragen. Als britische Truppen 1860 die "
        "Verbotene Stadt betraten, wurden fünf Palasthunde nach Großbritannien "
        "gebracht, einer davon an Königin Victoria. 1893 wurde die Rasse in "
        "Großbritannien anerkannt und ist seither ein beliebter Begleiter."
    ),
    "pembroke-welsh-corgi": (
        "Der Pembroke Welsh Corgi ist ein Treibhund aus Pembrokeshire in Wales, "
        "wo er Rinder auf die Weide und zum Markt trieb, indem er ihnen in die "
        "Fersen zwickte. Eine alte walisische Legende erzählt, die Hunde seien "
        "ein Geschenk der Feen, und Bauern hielten sie jahrhundertelang als "
        "zähe, niedrige Arbeitshunde. 1934 wurden die beiden walisischen "
        "Corgi-Rassen getrennt, und der Pembroke wurde international anerkannt. "
        "Königin Elisabeth II. hielt jahrzehntelang Pembrokes, was die Rasse in "
        "der ganzen Welt bekannt machte."
    ),
    "pomeranian": (
        "Der Pomeranian ist nach Pommern benannt, der Region an der Ostseeküste "
        "zwischen Deutschland und Polen, wo große weiße Spitze als Schaf- und "
        "Schlittenhunde gehalten wurden. Züchter in Europa und Großbritannien "
        "machten den Hund im 19. Jahrhundert zunehmend kleiner und dekorativer. "
        "Der kleine Pomeranian von Königin Victoria, den sie aus Italien "
        "mitbrachte, gilt als Auslöser der Mode für die Zwergengröße. 1870 wurde "
        "die Rasse in Großbritannien anerkannt; heute ist sie eine der kleinsten "
        "Begleithunderassen der Welt."
    ),
    "poodle": (
        "Der Pudel stammt von alten europäischen Wasserhunden ab, und sein Name "
        "geht auf das deutsche Wort pudeln zurück, das Platschen im Wasser "
        "bedeutet. Er arbeitete in Deutschland als Retriever und später in "
        "Frankreich als Zirkus- und Begleithund, wo er zur Nationalrasse wurde. "
        "Die typische Löwenschur war ursprünglich praktisch: Brust und Gelenke "
        "blieben behaart, damit der Hund im kalten Wasser warm blieb. 1904 wurde "
        "die Rasse in Deutschland standardisiert; heute wird sie in drei Größen "
        "gezüchtet: Großpudel, Kleinpudel und Zwergpudel."
    ),
    "portuguese-podengo": (
        "Der Portugiesische Podengo ist eine alte iberische Jagdrasse, und Hunde "
        "dieses Typs wurden in Portugal bereits im Mittelalter beschrieben. Er "
        "wird in drei Größen gezüchtet: Der kleine Podengo jagt Kaninchen in "
        "Meuten, der große wurde auf Rot- und Schwarzwild eingesetzt. Die Hunde "
        "fuhren mit portugiesischen Seefahrern auf ihren Reisen. 1955 wurde die "
        "Rasse in Portugal standardisiert; sie ist bis heute ein robuster "
        "Arbeitshund und ein lebhafter Begleiter."
    ),
    "pug": (
        "Der Mops stammt aus China, wo kurzgesichtige Hunde an Kaiserhöfen "
        "gehalten und entlang der Seidenstraße gehandelt wurden. Niederländische "
        "und portugiesische Händler brachten sie im 16. Jahrhundert nach Europa, "
        "und die Rasse wurde zum Liebling des niederländischen Hofes — ein Mops "
        "soll Wilhelm von Oranien vor einem spanischen Angriff gewarnt haben. In "
        "England wurde der Mops im 19. Jahrhundert kleiner gezüchtet und 1885 "
        "anerkannt. Heute ist er eine der bekanntesten Kleinhunderassen der Welt."
    ),
    "puli": (
        "Der Puli ist ein ungarischer Hütehund zentralasiatischer Herkunft, den "
        "die Magyaren vor über tausend Jahren ins Karpatenbecken brachten. Sein "
        "Schnurfell schützt ihn vor Wetter und vor den Zähnen der Schafe, die er "
        "treibt, und er arbeitet schnell und springend. Im 20. Jahrhundert ging "
        "die Rasse fast verloren, wurde aber ab den 1920er Jahren in Ungarn "
        "wieder aufgebaut. Ein ungarischer Puli war an der Forschung beteiligt, "
        "aus der das moderne Clickertraining entstand."
    ),
    "rat-terrier": (
        "Der Rat Terrier ist ein amerikanischer Hofhund des frühen 20. "
        "Jahrhunderts, der aus Terriern, Feists und anderen kleinen Jagdhunden "
        "der Siedler entstand. Seinen Namen verdient er sich damit, dass er "
        "Scheunen und Kornspeicher von Ratten befreite; außerdem arbeitete er auf "
        "Eichhörnchen und Kaninchen und bewachte den Hof. In den 1920er und "
        "1930er Jahren war die Rasse beliebt, geriet dann in Vergessenheit, bis "
        "Züchter sie in den 1990er Jahren zurückbrachten. Sie ist ein robuster, "
        "anspruchsloser Arbeits- und Familienhund."
    ),
    "romagna-water-dog": (
        "Der Romagna-Wasserhund, der Lagotto Romagnolo, stammt aus dem Tiefland "
        "der Romagna in Nordostitalien, wo er jahrhundertelang Wasservögel aus "
        "den Sümpfen aufstöberte. Als die Sümpfe im 20. Jahrhundert trockengelegt "
        "wurden, bekamen die Hunde eine neue Aufgabe: die Suche nach Trüffeln, "
        "die sie ausschließlich mit der Nase finden. 1991 wurde die Rasse in "
        "Italien anerkannt, 2005 international. Sie ist die einzige Hunderasse, "
        "die traditionell für die Trüffelsuche eingesetzt wird."
    ),
    "rottweiler": (
        "Der Rottweiler stammt von römischen Treibhunden ab, die für die "
        "Legionen Vieh bewachten und trieben, und einige von ihnen blieben in der "
        "deutschen Stadt Rottweil. Dort wurden sie zu Metzgerhunden: Sie trieben "
        "das Vieh zum Markt und zogen Karren mit Fleisch, wobei das Geld am Halsband "
        "befestigt wurde. Als Eisenbahnen und Treibverbote diese Arbeit beendeten, "
        "verschwand die Rasse fast, und 1901 wurde ein Verein zu ihrer Rettung "
        "gegründet. 1901 wurde sie in Deutschland anerkannt und entwickelte sich "
        "zu einer weltberühmten Polizei-, Dienst- und Wachhunderasse."
    ),
    "saint-bernard": (
        "Der Bernhardiner ist nach dem Hospiz benannt, das im 11. Jahrhundert von "
        "Bernhard von Menthon hoch in den Schweizer Alpen gegründet wurde. Die "
        "Mönche hielten große Berghunde zur Bewachung des Passes und setzten sie "
        "ab dem 17. Jahrhundert ein, um im Schnee verlorene Reisende zu finden. "
        "Der berühmteste von ihnen, Barry, soll mehr als vierzig Menschen "
        "gerettet haben, und noch heute wird die Rasse mit dem legendären "
        "Brandy-Fässchen verbunden. 1884 wurde sie in der Schweiz "
        "standardisiert; sie ist der Nationalhund des Landes."
    ),
    "samoyed": (
        "Der Samojede ist nach den samojedischen Völkern Sibiriens benannt, die "
        "weiße, lächelnde Spitze für das Hüten von Rentieren, das Ziehen von "
        "Schlitten und das Bewachen des Lagers züchteten. Die Hunde lebten eng "
        "mit den Familien und schliefen sogar in den Zelten, weshalb die Rasse "
        "besonders menschenbezogen ist. Ende des 19. Jahrhunderts brachten "
        "Forscher sie aus Sibirien heraus, und 1909 wurde der erste Standard in "
        "Großbritannien verfasst. Samojeden nahmen an mehreren Polar-Expeditionen "
        "teil, darunter am Antarktisversuch von Scott."
    ),
    "scottish-terrier": (
        "Der Scottish Terrier stammt aus dem Hochland und von den Inseln "
        "Schottlands, wo mehrere kurzbeinige Terriertypen in Steinhaufen und "
        "Bauen arbeiteten. Im 19. Jahrhundert wurden sie getrennt, und der "
        "Aberdeen Terrier wurde zum Scottish Terrier, wie wir ihn kennen. Der "
        "erste Standard wurde 1880 veröffentlicht, 1882 folgte die Anerkennung "
        "in Großbritannien. Sein robuster Charakter und die berühmte Silhouette "
        "machten ihn zum Symbol Schottlands und zum Liebling von Präsidenten und "
        "Schriftstellern."
    ),
    "shar-pei": (
        "Der Shar Pei ist eine alte chinesische Rasse aus der südlichen Provinz "
        "Guangdong, wo Hunde mit lockerer, faltiger Haut und blau-schwarzer Zunge "
        "für Jagd, Hüten und Bewachen gehalten wurden. Nach der chinesischen "
        "Revolution verschwand die Rasse fast, und in den 1970er Jahren gab es "
        "nur noch wenige Hunde in Hongkong und Macau. Züchter retteten sie mit "
        "Unterstützung des Hongkonger Kennel Clubs, und 1991 wurde der Shar Pei "
        "in den USA anerkannt. Heute wird er vor allem als Begleithund gehalten."
    ),
    "shih-tzu": (
        "Der Shih Tzu wurde in den Palästen Chinas gezüchtet und wird oft mit "
        "der buddhistischen Tradition verbunden, in der ein kleiner "
        "löwenähnlicher Hund ein Schutzsymbol war. Hofzüchter kreuzten tibetische "
        "Hunde mit Pekinesen, um die heutige Rasse zu schaffen, und "
        "jahrhundertelang hielten Kaiser und Adel diese Hunde. In den 1920er und "
        "1930er Jahren kamen einige Hunde nach Großbritannien, wo die Rasse 1946 "
        "anerkannt wurde. Sein Name bedeutet kleiner Löwe."
    ),
    "siberian-husky": (
        "Der Siberian Husky wurde vom Volk der Tschuktschen im Nordosten "
        "Sibiriens für leichte Schlitten über enorme Strecken bei wenig Futter "
        "gezüchtet. Die Hunde lebten mit den Familien und wurden für Ausdauer, "
        "freundliches Wesen und dichtes Doppelfell geschätzt. 1909 kamen sie für "
        "Schlittenrennen nach Alaska, und 1925 brachten Huskyschlitten in einer "
        "Staffel Diphtherie-Serum nach Nome. 1930 wurde die Rasse in den USA "
        "anerkannt; heute ist sie ein beliebter Begleit- und Sporthund."
    ),
    "sloughi": (
        "Der Sloughi ist ein Windhund des Maghreb, den Berber und Beduinen in "
        "Marokko, Algerien, Tunesien und Libyen hielten. Er jagt Hasen, Gazellen "
        "und Wildschweine im offenen Land und lebt eng mit der Familie, wobei er "
        "nachts das Lager bewacht. Die Rasse wird in der arabischen Dichtung "
        "erwähnt und kam im 19. Jahrhundert nach Europa. Ein französischer Club "
        "wurde 1927 gegründet, 1935 folgte die internationale Anerkennung."
    ),
    "treeing-walker-coonhound": (
        "Der Treeing Walker Coonhound wurde in den USA aus virginischen "
        "Laufhunden entwickelt, die Siedler nach Westen brachten, vor allem aus "
        "den Walker-Hunden aus Kentucky. Jäger wollten einen schnellen Hund mit "
        "feiner Nase, der die Fährte von Waschbär und Bär halten und das Tier "
        "dann verbellen konnte. 1945 wurde die Rasse unter eigenem Namen "
        "registriert und ist einer der beliebtesten Coonhounds Amerikas. Sie "
        "bleibt vor allem ein Jagdhund mit sanftem Wesen im Haus."
    ),
    "weimaraner": (
        "Der Weimaraner stammt vom Hof in Weimar in Deutschland, wo Adlige im "
        "19. Jahrhundert einen vielseitigen Jagdhund für großes Wild, Federwild "
        "und Wasserarbeit züchteten. Deutsche Züchter hielten die Rasse streng "
        "unter Kontrolle: Bevor ein Welpe verkauft wurde, musste er Feldprüfungen "
        "bestehen, und seine Eltern mussten sich in der Arbeit bewährt haben. Der "
        "erste Club entstand 1897, 1929 kam die Rasse in die USA. Der graue Geist "
        "mit samtigem Fell wurde ein auffälliger Jagd- und Begleithund."
    ),
    "whippet": (
        "Der Whippet stammt aus Nordengland, wo Bergleute im 19. Jahrhundert "
        "einen kleinen, ruhigen Windhund züchteten, den man in einem kleinen Haus "
        "halten und nach der Schicht auf gerader Bahn rennen lassen konnte. Er "
        "entstand aus Greyhounds und Terriern und wurde zur Kaninchenhetze "
        "genutzt, die man Snap-Dog nannte. In den 1890er Jahren entstanden "
        "Rennclubs, und 1891 wurde die Rasse in Großbritannien anerkannt. Er ist "
        "der schnellste Hund seiner Größe und einer der ruhigsten im Haus."
    ),
    "wire-fox-terrier": (
        "Der Drahthaar-Foxterrier ist ein britischer Terrier aus den "
        "Fuchsjagdgebieten Englands, wo seine Aufgabe darin bestand, den Fuchs aus "
        "dem Bau zu treiben, damit die Hunde die Hetze fortsetzen konnten. Die "
        "glatte und die rauhaarige Varietät wurden durch Clubs getrennt, die 1876 "
        "gegründet wurden, und die rauhaarige wurde die beliebtere. 1877 wurde "
        "sie in Großbritannien anerkannt und bald zum führenden Ausstellungshund, "
        "der auf der Crufts mehr Best-in-Show-Titel gewann als jede andere "
        "Rasse."
    ),
    "xoloitzcuintli": (
        "Der Xoloitzcuintli, der Mexikanische Nackthund, ist eine der ältesten "
        "Hunderassen Amerikas: Nackthunde wurden in Mexiko seit mehr als "
        "dreitausend Jahren gehalten. Die Azteken benannten sie nach dem Gott "
        "Xolotl und glaubten, sie geleiteten Seelen; außerdem dienten sie als "
        "Heiler und Begleiter. Im 20. Jahrhundert verschwand die Rasse fast und "
        "wurde ab den 1950er Jahren von mexikanischen Züchtern gerettet. 1956 "
        "wurde sie in Mexiko anerkannt; heute wird sie in drei Größen gezüchtet, "
        "nackt und behaart."
    ),
    "yakutian-laika": (
        "Die Jakutische Laika ist eine alte Landrasse aus der Republik Sacha in "
        "Sibirien, wo sie an einem der kältesten bewohnten Orte der Erde "
        "arbeitete. Die Hunde zogen Schlitten, jagten Wassergeflügel und hüteten "
        "vor allem Rentiere, wobei sie in extremer Kälte neben den Familien "
        "lebten. In der Sowjetzeit ging die Rasse fast verloren, und russische "
        "Züchter begannen in den 1990er Jahren mit dem Wiederaufbau. 2005 wurde "
        "sie in Russland anerkannt, 2019 international; außerhalb Sibiriens ist "
        "sie noch selten."
    ),
    "yorkshire-terrier": (
        "Der Yorkshire Terrier entstand im Norden Englands im 19. Jahrhundert, "
        "als schottische Weber mit ihren kleinen Terriern nach Yorkshire zogen. "
        "Arbeiter kreuzten sie mit einheimischen Terriern, um einen winzigen "
        "Rattenfänger für Fabriken und Bergwerke zu bekommen, und bis 1870 wurde "
        "die Rasse als Broken-Haired Scotch Terrier ausgestellt. 1886 wurde sie "
        "in Großbritannien anerkannt und bald zum modischen Begleiter. Heute ist "
        "sie eine der kleinsten Rassen der Welt und ein beliebter Schoßhund."
    ),
    "brussels-griffon": (
        "Der Brüsseler Griffon stammt aus Belgien, wo Kutscher im 19. Jahrhundert "
        "kleine, rauhaarige Hunde in den Ställen hielten, um Ratten zu jagen und "
        "vor Fremden zu warnen. Die Rasse entstand aus dem Griffon d'Écurie, dem "
        "belgischen Straßenhund und dem kleinen Mops, der ihr das kurze Gesicht "
        "und den fast menschlichen Ausdruck gab. Es entwickelten sich zwei "
        "Fellarten, und die glatte heißt heute Petit Brabançon. 1904 wurde die "
        "Rasse in Belgien anerkannt, und der Film Besser geht's nicht machte sie "
        "weltbekannt."
    ),
    # <<< END DE >>>
}

HISTORY_IT = {
    "afghan-hound": (
        "Il Levriero Afgano è uno dei levrieri più antichi: incisioni e testi "
        "mostrano che cani di questa forma vivevano in Afghanistan e nelle "
        "montagne vicine già migliaia di anni fa. I cacciatori locali li usavano "
        "per inseguire lepri e gazzelle su terreni sassosi e impervi, dove la "
        "sola velocità non bastava. Gli ufficiali britannici portarono la razza in "
        "patria alla fine dell'Ottocento, e i primi afgani furono esposti in "
        "Inghilterra nel 1907. Il Kennel Club riconobbe la razza nel 1926, e il "
        "suo aspetto aristocratico ne fece un'icona di moda negli anni Sessanta "
        "e Settanta."
    ),
    "airedale-terrier": (
        "L'Airedale Terrier proviene dalla valle del fiume Aire nello Yorkshire, "
        "dove nell'Ottocento gli operai incrociarono l'Old English Black and Tan "
        "Terrier, oggi estinto, con l'Otterhound. L'obiettivo era un cane capace "
        "di cacciare lontre e ratti, di lavorare con il fucile e di custodire il "
        "cortile. Fu chiamato il re dei terrier, e nella Prima guerra mondiale "
        "l'esercito britannico lo impiegò come cane da staffetta e di guardia. La "
        "razza fu riconosciuta in Gran Bretagna nel 1886 e in seguito si diffuse "
        "come cane da famiglia e da polizia."
    ),
    "akita": (
        "L'Akita è allevato nel nord del Giappone da secoli ed è legato alle "
        "zone montuose della prefettura di Akita, dove veniva usato per la caccia "
        "all'orso, al cinghiale e al cervo. Nella tradizione giapponese la razza "
        "era simbolo di salute e buona fortuna, e ancora oggi se ne regalano "
        "piccole statuette. Dopo la Seconda guerra mondiale la razza rischiò di "
        "scomparire e fu ricostruita da poche linee sopravvissute. L'Akita più "
        "famoso, Hachiko, attese il padrone per quasi dieci anni in una stazione "
        "di Tokyo e oggi ha una statua in bronzo."
    ),
    "alaskan-malamute": (
        "L'Alaskan Malamute prende il nome dagli Inuit Mahlemut dell'Alaska, che "
        "allevavano cani da traino pesanti molto prima dell'arrivo degli "
        "europei. Questi cani trainavano slitte cariche di carne, pelli e "
        "attrezzature e all'inizio del Novecento parteciparono anche a "
        "spedizioni polari. Durante la corsa all'oro del Klondike la razza fu "
        "incrociata con cani da slitta più piccoli e veloci e perse quasi il suo "
        "tipo originale. Negli anni Venti e Trenta gli allevatori riportarono il "
        "Malamute pesante e potente, e nel 1935 la razza fu riconosciuta negli "
        "Stati Uniti."
    ),
    "american-cocker-spaniel": (
        "L'American Cocker Spaniel discende da cani portati in Nord America "
        "dall'Inghilterra nell'Ottocento, quando il cocker era ancora una sola "
        "razza con l'English Cocker. Gli allevatori americani volevano un cane "
        "più piccolo e dal pelo setoso per la caccia alla beccaccia nel folto. I "
        "due tipi si separarono e nel 1946 l'American Cocker fu riconosciuto come "
        "razza a sé. Divenne uno dei cani da compagnia più popolari del "
        "Novecento e il modello della cagnolina Lady della Disney."
    ),
    "american-eskimo-dog": (
        "L'American Eskimo Dog discende da spitz bianchi portati negli Stati "
        "Uniti dagli immigrati tedeschi nell'Ottocento. Questi cani si "
        "esibivano nei circhi itineranti, e grazie ai loro numeri il piccolo cane "
        "bianco divenne famoso in tutto il Paese. Con il crescere del sentimento "
        "antitedesco durante la Prima guerra mondiale il nome passò da Spitz "
        "tedesco ad American Eskimo. La razza fu riconosciuta negli Stati Uniti "
        "nel 1995 ed è ancora apprezzata come cane di famiglia e da guardia."
    ),
    "american-staffordshire-terrier": (
        "L'American Staffordshire Terrier risale ai bull-and-terrier portati negli "
        "Stati Uniti dall'Inghilterra nell'Ottocento. Gli allevatori americani "
        "crearono un cane più alto e pesante dell'originale inglese e lo usarono "
        "in fattoria, in famiglia e nel ring. Fu registrato prima come American "
        "Bull Terrier e poi come Staffordshire Terrier. Il nome American "
        "Staffordshire Terrier fu adottato nel 1969 per distinguerlo dallo "
        "Staffordshire Bull Terrier inglese, e la razza divenne un popolare cane "
        "da famiglia."
    ),
    "anatolian-shepherd-dog": (
        "Il Pastore dell'Anatolia è un antico cane da guardiania degli altopiani "
        "dell'Anatolia, in Turchia. Per secoli ha vissuto con i pastori e le "
        "loro greggi, difendendo le pecore da lupi e orsi senza condurle. I cani "
        "erano selezionati per resistenza, indipendenza e capacità di lavorare da "
        "soli in un clima duro. Negli anni Settanta la Turchia iniziò a "
        "registrare la razza, che si diffuse in Europa e negli Stati Uniti come "
        "guardiano da lavoro e cane di famiglia calmo e imponente."
    ),
    "australian-shepherd": (
        "L'Australian Shepherd fu sviluppato negli Stati Uniti occidentali, non "
        "in Australia, anche se i suoi antenati erano cani da pastore baschi e "
        "australiani. Gli allevatori avevano bisogno di un cane capace di "
        "spostare pecore e bovini su lunghe distanze e di lavorare con caldo, "
        "polvere e neve. La razza era tenuta da famiglie di allevatori e da "
        "concorrenti di rodeo, e il nome le venne dal bestiame e dai pastori "
        "arrivati con le navi australiane. Fu riconosciuta negli Stati Uniti nel "
        "1991 ed è oggi una delle razze da pastore più conosciute."
    ),
    "azawakh": (
        "L'Azawakh è un levriero del Sahel, allevato dai Tuareg e da altri "
        "popoli nomadi del Mali, del Niger e del Burkina Faso. Caccia gazzelle e "
        "lepri nel deserto aperto e sorveglia l'accampamento, vivendo a stretto "
        "contatto con le persone. La razza prende il nome dalla valle dell'Azawakh "
        "e la sua struttura snella è adatta al caldo e alle lunghe distanze. I "
        "primi Azawakh arrivarono in Europa negli anni Settanta e la razza fu "
        "riconosciuta a livello internazionale nel 1981."
    ),
    "barbado-da-terceira": (
        "Il Barbado da Terceira proviene dall'isola di Terceira nelle Azzorre, "
        "dove fu allevato per lavorare con il bestiame su terreno vulcanico "
        "aspro. I contadini dell'isola avevano bisogno di un cane di taglia media "
        "capace di condurre la mandria, custodire la proprietà ed essere gentile "
        "con la famiglia. La razza rimase quasi sconosciuta fuori dalle Azzorre "
        "per secoli e fu salvata dagli allevatori locali nel Novecento. Il "
        "Portogallo la riconobbe nel 2004; oggi è un cane da pastore e da "
        "compagnia raro ma in crescita."
    ),
    "basset-hound": (
        "Il Basset Hound discende dai segugi francesi tenuti da abbazie e case "
        "nobili per la caccia al coniglio e al cervo. Il tipo basso e lento "
        "comparve in Francia nel Cinquecento e fu perfezionato nell'Ottocento, "
        "quando i cacciatori vollero un cane che potessero seguire a piedi. Gli "
        "allevatori britannici importarono la razza nel 1866 e le diedero "
        "l'aspetto moderno. Fu riconosciuto in Gran Bretagna nel 1880 e nel "
        "Novecento divenne un famoso cane pubblicitario e da famiglia."
    ),
    "bedlington-terrier": (
        "Il Bedlington Terrier fu sviluppato nella regione mineraria del "
        "Northumberland, in Inghilterra, e prende il nome dalla città di "
        "Bedlington. Minatori e bracconieri lo usavano per cacciare ratti, "
        "conigli e lontre, e il cane riusciva a infilarsi nelle tane più "
        "strette. Il pelo simile a quello di un agnello e il dorso arcuato "
        "nascondono un terrier tenace, un tempo chiamato Rothbury Terrier. Fu "
        "riconosciuto in Gran Bretagna nel 1877 e in seguito divenne cane da "
        "esposizione e da compagnia."
    ),
    "bichon-frise": (
        "Il Bichon Frisé discende da piccoli cani bianchi che marinai e "
        "commercianti portavano con sé nel Mediterraneo durante il Medioevo. Il "
        "tipo fu perfezionato in Francia, dove il bichon divenne il favorito "
        "della corte e poi degli artisti di strada e degli organettisti. Il pelo "
        "riccio e il carattere allegro lo resero un cane da circo molto amato. La "
        "razza fu riconosciuta in Francia nel 1933 e negli Stati Uniti nel 1972, "
        "ed è oggi un compagno molto amato."
    ),
    "black-and-tan-coonhound": (
        "Il Black and Tan Coonhound fu sviluppato negli Stati Uniti dai segugi "
        "europei portati dai coloni, in particolare dal Talbot Hound e dal "
        "Bloodhound. I cacciatori volevano un cane capace di seguire di notte la "
        "traccia del procione e dell'orso e poi di abbaiare sotto l'albero. La "
        "razza lavora esclusivamente con il naso ed è famosa per la voce profonda "
        "e costante sulla traccia. Fu riconosciuta negli Stati Uniti nel 1945 e "
        "resta un cane specializzato per la caccia."
    ),
    "bloodhound": (
        "Il Bloodhound è uno dei segugi più antichi: i suoi antenati erano "
        "descritti in Europa già nel VII secolo e furono perfezionati dai monaci "
        "in Belgio e in Francia. Il nome indica un ceppo puro e nobile, non il "
        "sangue. Per secoli è stato usato per seguire le tracce di cervi, "
        "cinghiali e poi di persone, e le sue prove sono state accettate in "
        "tribunale. La razza fu standardizzata in Gran Bretagna nel 1897 ed è "
        "ancora oggi il riferimento per il lavoro su traccia."
    ),
    "bolognese": (
        "Il Bolognese è un piccolo cane bianco da compagnia originario di "
        "Bologna, e i suoi antenati compaiono nell'arte italiana del "
        "Rinascimento. Le famiglie nobili lo tenevano come cane da grembo e lo "
        "regalavano alle altre corti europee come dono diplomatico. La razza "
        "rischiò di scomparire nell'Ottocento e fu ricostruita da poche linee "
        "sopravvissute nel Novecento. In Italia fu riconosciuto nel 1956, e fuori "
        "dalla patria è ancora raro."
    ),
    "border-collie": (
        "Il Border Collie nacque al confine tra Inghilterra e Scozia, dove i "
        "pastori avevano bisogno di un cane capace di guidare il gregge in "
        "collina con un solo comando o fischio. La selezione puntava "
        "sull'intelligenza, sulla resistenza e soprattutto su uno sguardo "
        "silenzioso e controllante chiamato eye. Il nome si affermò nel 1915; "
        "prima i cani erano semplicemente chiamati working collie. La razza è "
        "ancora il riferimento nelle gare di conduzione del gregge, e uno dei "
        "suoi esemplari, Chaser, imparò i nomi di oltre mille giochi."
    ),
    "border-terrier": (
        "Il Border Terrier proviene dalle Cheviot Hills, al confine tra "
        "Inghilterra e Scozia, dove lavorava con i foxhound e cacciava le volpi "
        "che minacciavano le pecore. Doveva essere abbastanza stretto da seguire "
        "la volpe nella tana e abbastanza resistente da correre tutto il giorno "
        "con i cavalli. Fu esposto come Coquetdale Terrier e prese il nome Border "
        "nel 1880. Fu riconosciuto in Gran Bretagna nel 1920 ed è ancora un "
        "terrier da lavoro e un solido cane di famiglia."
    ),
    "borzoi": (
        "Il Borzoi, o Levriero Russo, fu creato dai nobili russi incrociando "
        "levrieri arabi e persiani con cani da caccia locali a pelo folto. Era "
        "usato nella caccia al lupo, lavorando in coppia o in piccoli branchi "
        "insieme ai cacciatori a cavallo. La razza era tenuta quasi solo "
        "dall'aristocrazia e la rivoluzione del 1917 rischiò di cancellarla. I "
        "cani sopravvissuti furono esportati negli anni Venti, e nel Novecento la "
        "razza si affermò come elegante cane da esposizione e da compagnia."
    ),
    "boxer": (
        "Il Boxer fu sviluppato in Germania nell'Ottocento dal Bullenbeisser e "
        "dal Bulldog inglese. Gli allevatori di Monaco volevano un potente cane "
        "da guardia e da conduzione del bestiame, con testa corta e pulita e "
        "carattere equilibrato. Il primo boxer fu registrato nel 1904 e la razza "
        "si diffuse rapidamente come cane da polizia e da guerra. Nella Prima "
        "guerra mondiale servì come staffetta e sentinella, e dopo il conflitto "
        "divenne uno dei cani da famiglia più popolari in Europa e in Nord "
        "America."
    ),
    "bulldog": (
        "Il Bulldog inglese discende dagli antichi cani di tipo mastino usati per "
        "il bull-baiting, uno spettacolo crudele vietato in Gran Bretagna nel "
        "1835. Quando lo spettacolo finì, gli allevatori trasformarono il cane in "
        "un docile compagno e gli diedero la forma pesante e dal muso corto che "
        "conosciamo. Il primo club di razza nacque nel 1875 e il Bulldog divenne "
        "simbolo nazionale della Gran Bretagna, paragonato nelle caricature al "
        "carattere del Paese. L'allevamento moderno punta su salute, respirazione "
        "e mobilità."
    ),
    "bull-terrier": (
        "Il Bull Terrier fu creato nell'Inghilterra dell'Ottocento incrociando "
        "l'antico bull-and-terrier con il White English Terrier, oggi estinto. "
        "James Hinks voleva un cane completamente bianco e atletico con la testa "
        "a forma di uovo, e la razza fu riconosciuta in Gran Bretagna nel 1887. I "
        "cani colorati furono aggiunti nel Novecento e registrati come "
        "Staffordshire Bull Terrier. Il Bull Terrier divenne famoso come cane "
        "sportivo e mascotte militare e in seguito come elegante compagno "
        "cittadino."
    ),
    "cane-corso": (
        "Il Cane Corso proviene dall'Italia meridionale e discende dagli antichi "
        "molossi romani usati per la guardia, la caccia e la guerra. Il suo nome "
        "risale alla parola latina per guardia del corpo, e per secoli ha "
        "lavorato nelle fattorie, conducente il bestiame e proteggendo le "
        "proprietà. Dopo la Seconda guerra mondiale la razza rischiò di sparire e "
        "fu salvata dagli appassionati italiani negli anni Settanta. Nel 1987 "
        "l'Italia definì lo standard, e oggi il Cane Corso è un guardiano e cane "
        "di famiglia diffuso in tutto il mondo."
    ),
    "catahoula-leopard-dog": (
        "Il Catahoula Leopard Dog è il cane ufficiale della Louisiana e prende il "
        "nome dalla parrocchia di Catahoula. Nacque da cani di esploratori "
        "spagnoli, coloni francesi e ceppi nativi americani, e il suo mantello "
        "macchiettato è unico tra le razze da lavoro. Con lui si conducono maiali "
        "selvatici e bovini nelle paludi e nei boschi di pino, lavorando in "
        "muta. Fu riconosciuto ufficialmente negli Stati Uniti nel 1979 e resta "
        "soprattutto un cane da lavoro."
    ),
    "cavalier-king-charles-spaniel": (
        "Il Cavalier King Charles Spaniel riporta in vita i piccoli spaniel da "
        "compagnia dipinti accanto alla nobiltà europea nel Cinquecento e "
        "Seicento. Re Carlo II li amava tanto che il tipo prese il suo nome. Nel "
        "Novecento l'English Toy Spaniel dal muso piatto aveva sostituito "
        "l'aspetto antico, e gli allevatori americani offrirono un premio per i "
        "cani con il muso lungo dei vecchi dipinti. Il Cavalier fu riconosciuto "
        "in Gran Bretagna nel 1945 ed è da allora una delle razze da compagnia "
        "più popolari."
    ),
    "collie-rough": (
        "Il Collie a pelo lungo è un cane da pastore scozzese delle Highlands, "
        "dove lavorava con le pecore in collina e con qualsiasi tempo. La razza "
        "fu perfezionata nell'Ottocento, e la predilezione della regina Vittoria "
        "per questi cani li rese di moda anche fuori dalla Scozia. Il nome "
        "deriva dall'antica parola scozzese per un utile cane da pastore bianco e "
        "nero. Fu riconosciuto in Gran Bretagna nel 1874, e i romanzi e i film su "
        "Lassie trasformarono il Collie nel simbolo mondiale del cane di famiglia "
        "fedele."
    ),
    "czechoslovakian-wolfdog": (
        "Il Cane da lupo cecoslovacco nacque nel 1955 come esperimento militare "
        "in Cecoslovacchia, incrociando il Pastore tedesco con il lupo dei "
        "Carpazi. Scopo era unire l'addestrabilità del pastore alla resistenza e "
        "ai sensi del lupo per il servizio di confine. L'incrocio riuscì, ma i "
        "cani si rivelarono difficili da addestrare e non furono mai usati in "
        "gran numero dall'esercito. La razza fu riconosciuta in Cecoslovacchia "
        "nel 1982 e a livello internazionale nel 1999; oggi è un cane da lavoro e "
        "da compagnia esigente."
    ),
    "dachshund": (
        "Il Bassotto fu sviluppato in Germania nel corso di vari secoli da cani da "
        "caccia bassi, capaci di seguire tassi e volpi nella tana. Il nome "
        "significa cane da tasso e la razza compare nei documenti tedeschi dal XV "
        "secolo. Furono selezionati tre tipi di pelo e due taglie per selvaggina "
        "diversa, e i cani lavoravano anche in muta su cinghiali e cervi. Fu "
        "riconosciuto in Gran Bretagna nel 1881 e divenne un amatissimo cane di "
        "famiglia, lungo, basso e molto affezionato."
    ),
    "dalmatian": (
        "Il Dalmata prende il nome dalla regione adriatica della Dalmazia, e cani "
        "di questo tipo macchiato compaiono in dipinti e registri parrocchiali "
        "del Seicento e Settecento. La razza era usata come cane da carrozza: "
        "correva accanto o sotto l'asse, liberava la strada e sorvegliava i "
        "cavalli nelle locande. Gli allevatori britannici la standardizzarono "
        "nell'Ottocento e fu riconosciuta nel 1888. Il legame con i vigili del "
        "fuoco nacque quando i carri antincendio trainati da cavalli tenevano "
        "dalmata per calmare i cavalli."
    ),
    "dobermann": (
        "Il Dobermann fu creato negli anni Novanta dell'Ottocento da Karl "
        "Friedrich Louis Dobermann, esattore delle tasse e accalappiacani "
        "tedesco di Apolda. Aveva bisogno di un guardiano impavido e intelligente "
        "che lo accompagnasse nei giri pericolosi, e costruì la razza da diversi "
        "tipi da guardia e da caccia. Il primo club nacque nel 1899 e il cane si "
        "diffuse rapidamente come cane da polizia e da guerra. Fu riconosciuto a "
        "livello internazionale all'inizio del Novecento e resta uno dei cani da "
        "difesa e da servizio più stimati."
    ),
    "drever": (
        "Il Drever è un segugio svedese nato dal Dachsbracke di Westfalia e da "
        "altri cani da caccia tedeschi arrivati al nord nell'Ottocento. I "
        "cacciatori svedesi volevano un segugio basso e tranquillo capace di "
        "seguire caprioli e lepri nella neve e nel bosco fitto a un passo che un "
        "uomo potesse seguire. Per anni fu chiamato Dachsbracke svedese e nel "
        "1947 prese il nome Drever. In Svezia è riconosciuto a livello nazionale "
        "ed è uno dei cani da caccia più diffusi del Paese."
    ),
    "dutch-shepherd-dog": (
        "Il Pastore olandese è la razza da pastore dei Paesi Bassi, allevata in "
        "tre varietà di pelo: corto, lungo e ruvido. I contadini li tenevano per "
        "condurre pecore e bovini, custodire il cortile e trainare piccoli "
        "carri, e li usarono anche come cani di polizia e da staffetta. Nel 1898, "
        "con la fondazione del club olandese, la razza fu standardizzata, e dopo "
        "la Seconda guerra mondiale il numero calò bruscamente. L'allevamento "
        "riprese negli anni Settanta, e oggi la razza lavora con polizia e "
        "unità di ricerca."
    ),
    "english-setter": (
        "L'English Setter fu sviluppato in Gran Bretagna nell'arco di oltre "
        "quattrocento anni da cani che si accucciavano quando trovavano la "
        "selvaggina, permettendo al cacciatore di gettare la rete sugli uccelli. "
        "Nell'Ottocento Edward Laverack e Purcell Llewellin crearono le due "
        "linee da cui discendono quasi tutti i setter moderni. La razza fu "
        "riconosciuta in Gran Bretagna nel 1874. È nota per il carattere dolce e "
        "per il mantello macchiettato belton, e ancora oggi lavora come cane da "
        "ferma e vive come cane di famiglia."
    ),
    "french-bulldog": (
        "Il Bouledogue francese iniziò come piccolo bulldog inglese tenuto dalle "
        "merlettaie di Nottingham, che negli anni Sessanta dell'Ottocento "
        "portarono i cani con sé in Francia. A Parigi i cani diventarono i "
        "favoriti della società e degli artisti, e gli allevatori francesi "
        "selezionarono le orecchie erette a pipistrello e il corpo compatto. La "
        "razza fu riconosciuta in Francia e negli Stati Uniti nel 1898. Dopo un "
        "calo di popolarità all'inizio del Novecento, oggi è una delle razze da "
        "compagnia più diffuse al mondo."
    ),
    "german-shepherd-dog": (
        "Il Pastore tedesco fu fondato nel 1899 da Max von Stephanitz, che "
        "voleva un cane da lavoro e da pastore di grande intelligenza e "
        "resistenza. Comprò il cane Hektor, lo ribattezzò Horand von Grafrath e "
        "con il club SV dimostrò il valore della razza nel servizio. Il cane si "
        "diffuse rapidamente come cane da polizia, da guerra e guida per "
        "ciechi, e divenne famoso in entrambe le guerre mondiali. All'inizio del "
        "Novecento la razza fu riconosciuta a livello internazionale e resta una "
        "delle più impiegate nel lavoro."
    ),
    "german-shorthaired-pointer": (
        "Il Bracco tedesco a pelo corto proviene dalla Germania dell'Ottocento, "
        "dove il cacciatore aveva bisogno di un solo cane per tutto: ferma, "
        "riporto, traccia e lavoro in acqua. La razza fu costruita su antichi "
        "cani da ferma, segugi e cani d'acqua tedeschi, e il principe Albrecht "
        "zu Solms-Braunfels ne guidò lo sviluppo. Il primo libro genealogico fu "
        "pubblicato nel 1872. Fu riconosciuto negli Stati Uniti nel 1930 ed è "
        "oggi uno dei cani da caccia più versatili al mondo."
    ),
    "german-spitz": (
        "Lo Spitz tedesco appartiene alla più antica famiglia canina "
        "dell'Europa centrale, il tipo spitz tenuto per secoli attorno a case e "
        "fattorie. La razza si divide per taglia in Wolfspitz, grande, medio, "
        "piccolo e Pomerania, e tutti condividono orecchie erette, pelo folto e "
        "coda arricciata. Gli spitz lavoravano come cani da guardia, da pastore e "
        "da compagnia, e la loro immagine compare nell'arte tedesca del "
        "Medioevo. La razza fu standardizzata in Germania nel 1899 e riconosciuta "
        "a livello internazionale nel Novecento."
    ),
    "golden-retriever": (
        "Il Golden Retriever fu creato nelle Highlands scozzesi nella seconda metà "
        "dell'Ottocento da Dudley Marjoribanks, poi Lord Tweedmouth. Incrociò un "
        "retriever giallo a pelo ondulato con il Tweed Water Spaniel, oggi "
        "estinto, per ottenere un cane docile adatto al riporto da terra e "
        "dall'acqua. La prima cucciolata nacque nel 1868 e la linea rimase privata "
        "per decenni. La razza fu riconosciuta in Gran Bretagna nel 1913 ed è "
        "oggi uno dei cani da famiglia, da guida e da ricerca più amati al mondo."
    ),
    "great-dane": (
        "L'Alano fu sviluppato in Germania da antichi mastini e cani da caccia, e "
        "gli allevatori tedeschi fissarono il tipo moderno alla fine "
        "dell'Ottocento. Nonostante il nome inglese la razza è tedesca: si "
        "chiamava Deutsche Dogge, e nel 1880 un comitato a Berlino approvò il "
        "primo standard. Il cane era allevato per la caccia al cinghiale a "
        "cavallo e per la guardia delle tenute, e altezza e portamento tranquillo "
        "gli valsero il soprannome di Apollo dei cani. All'inizio del Novecento "
        "la razza fu riconosciuta a livello internazionale."
    ),
    "hovawart": (
        "L'Hovawart è un antico cane da fattoria tedesco il cui nome significa "
        "custode del cortile, e cani di questo tipo sono citati nei codici "
        "giuridici tedeschi del Medioevo. La razza moderna fu ricostruita negli "
        "anni Venti da allevatori che cercarono nella Foresta Nera e nello Harz "
        "cani corrispondenti alle antiche descrizioni. Furono incrociati con "
        "Pastori tedeschi, Terranova e Leonberger per fissare il tipo. La "
        "Germania riconobbe l'Hovawart nel 1937, e ancora oggi è tenuto "
        "soprattutto come cane da guardia e da famiglia."
    ),
    "irish-wolfhound": (
        "L'Irish Wolfhound è un antico levriero irlandese usato per cacciare "
        "lupi, alci e cinghiali, e compare nei documenti e nelle saghe irlandesi "
        "dei primi secoli dopo Cristo. I capi irlandesi regalavano questi cani ai "
        "re europei e inglesi, cosa che da un lato diffuse la razza e dall'altro "
        "la impoverì. Nell'Ottocento i lupi erano scomparsi e la razza rischiò "
        "l'estinzione; il capitano George Graham la ricostruì da linee "
        "sopravvissute e da levrieri simili. Fu riconosciuto in Gran Bretagna nel "
        "1886 ed è la più alta di tutte le razze."
    ),
    "italian-sighthound": (
        "Il Piccolo Levriero Italiano è un levriero di piccola taglia che "
        "compare nell'arte italiana fin dall'epoca romana ed era tenuto dalle "
        "famiglie nobili di tutta la penisola. Veniva usato per inseguire lepri e "
        "conigli e soprattutto come elegante compagno nelle corti di Firenze e "
        "Milano. La razza fu standardizzata in Italia nel 1928, e i primi cani "
        "arrivarono in Gran Bretagna negli anni Cinquanta. La sua struttura fine "
        "e il carattere tranquillo ne fanno oggi un cane da appartamento molto "
        "amato."
    ),
    "italian-spinone": (
        "Lo Spinone Italiano è un cane da ferma a pelo ruvido del Piemonte e "
        "della Lombardia, dove ha lavorato per secoli nei campi e nelle paludi "
        "del nord Italia. Cerca lentamente e da vicino, fa la ferma e riporta sia "
        "a terra sia in acqua, e un tempo era usato anche nella falconeria. Nel "
        "1950 in Italia fu approvato lo standard, quando il club si impegnò a "
        "salvarlo dall'estinzione dopo la guerra. È ancora un cane da caccia "
        "raro ma apprezzato e un dolce compagno di famiglia."
    ),
    "kai": (
        "Il Kai è uno spitz giapponese di taglia media originario delle montagne "
        "della prefettura di Yamanashi e prende il nome dall'antica provincia di "
        "Kai. Vi è allevato da secoli per la caccia al cervo e al cinghiale su "
        "terreni ripidi e nevosi. È una delle poche razze giapponesi con mantello "
        "tigrato ed è noto per l'indipendenza e l'agilità. Nel 1934 il Kai fu "
        "dichiarato monumento naturale in Giappone, e fuori dalla patria resta "
        "raro."
    ),
    "keeshond-wolfspitz": (
        "Il Keeshond, o Wolfspitz, è la più grande varietà dello Spitz tedesco e "
        "l'antico cane da chiatta dei Paesi Bassi. I barcaioli tenevano questi "
        "cani grigi dal muso di volpe sulle loro imbarcazioni come guardiani e "
        "compagni lungo canali e fiumi. Il nome olandese deriva da Kees de "
        "Gyselaer, un patriota del Settecento il cui cane divenne l'emblema di un "
        "movimento politico. Il primo standard fu scritto nel 1927, e oggi il "
        "Keeshond è tenuto soprattutto come vivace cane di famiglia."
    ),
    "kleiner-munsterlander": (
        "Il Kleiner Münsterländer è un antico cane da ferma versatile della "
        "regione di Münster, e cani da ferma di questo tipo compaiono nei dipinti "
        "tedeschi già nel Quattrocento. Lavora davanti al fucile, fa la ferma, "
        "riporta e segue la traccia del selvatico ferito, ed è usato anche nella "
        "caccia con il falco. Nel 1919 gli allevatori tedeschi definirono due "
        "taglie e il piccolo Münsterländer ottenne un club proprio. Oggi è un "
        "cane da caccia diffuso in Europa e un equilibrato cane di famiglia."
    ),
    "labrador-retriever": (
        "Il Labrador Retriever non viene dal Labrador ma da Terranova, dove "
        "piccoli cani d'acqua lavoravano con i pescatori e trainavano le reti in "
        "acqua gelida. I visitatori britannici li acquistarono all'inizio "
        "dell'Ottocento, e Lord Malmesbury e altri sportivi li allevarono per il "
        "riporto su terra e in acqua. Nel 1903 il Kennel Club registrò la razza. "
        "Da decenni è tra i cani da famiglia più popolari del mondo ed è "
        "largamente impiegato come guida, assistenza e soccorso."
    ),
    "nederlandse-kooikerhondje": (
        "Il Nederlandse Kooikerhondje è un antico cane di tipo spaniel olandese "
        "usato nelle anatre con le koje, le lunghe trappole a imbuto dei Paesi "
        "Bassi. Il cane attirava le anatre lungo il canale con la coda bianca "
        "piumata e restava silenzioso mentre il guardiano chiudeva la trappola. "
        "Nel Novecento la razza rischiò di scomparire e fu ricostruita da pochi "
        "cani dalla baronessa van Hardenbroek van Ammerstol dal 1939. I Paesi "
        "Bassi la riconobbero nel 1971; resta rara ma affascinante."
    ),
    "norwegian-elkhound-grey": (
        "Il Norvegese Elkhound Grigio è un antico spitz scandinavo ritrovato in "
        "sepolture risalenti a migliaia di anni fa. I cacciatori norvegesi lo "
        "usavano per trovare e fermare alci e orsi abbaiando con insistenza, e il "
        "cane sorvegliava anche le fattorie e custodiva il bestiame. Nel 1901 la "
        "razza fu standardizzata in Norvegia, e la varietà grigia è la più antica "
        "e diffusa delle due. All'inizio del Novecento fu riconosciuta a livello "
        "internazionale ed è apprezzata come cane da caccia e da famiglia."
    ),
    "nova-scotia-duck-tolling-retriever": (
        "Il Nova Scotia Duck Tolling Retriever fu sviluppato nella contea di "
        "Yarmouth, in Nuova Scozia, dove i cacciatori notarono che le volpi che "
        "giocavano sulla riva attiravano gli uccelli acquatici curiosi. Gli "
        "allevatori crearono un cane rosso che imita questo comportamento: si "
        "divincola sulla riva attirando le anatre a tiro e poi riporta la "
        "preda. La razza fu tenuta localmente per generazioni e riconosciuta in "
        "Canada nel 1945. È il più piccolo dei retriever e il cane ufficiale "
        "della Nuova Scozia."
    ),
    "old-english-sheepdog": (
        "L'Old English Sheepdog proviene dall'Inghilterra occidentale, dove "
        "conduceva bovini e pecore al mercato su lunghe distanze invece di "
        "custodirli nei campi. Il mantello folto lo proteggeva dal maltempo e "
        "dai morsi degli animali che spingeva, e la coda era tradizionalmente "
        "tagliata per indicare il cane da lavoro. La razza fu standardizzata in "
        "Gran Bretagna nel 1888 e divenne un cane da esposizione molto amato. Il "
        "suo carattere dolce e buffo lo rese poi un beniamino di famiglia."
    ),
    "otterhound": (
        "L'Otterhound è un antico segugio britannico, allevato per cacciare le "
        "lontre che svuotavano fiumi e stagni. Lavora in muta, seguendo la "
        "traccia a terra e la preda a vista nell'acqua, e il pelo ruvido e le "
        "zampe palmate gli permettono di restare ore nel bagnato. Nel 1978 la "
        "caccia alla lontra fu vietata in Gran Bretagna e la razza ebbe un "
        "crollo. Fu riconosciuta in Gran Bretagna nel 1910, ma oggi nel mondo "
        "esistono solo poche centinaia di cani: è una delle razze britanniche "
        "più rare."
    ),
    "pekingese": (
        "Il Pechinese fu tenuto per secoli nel palazzo imperiale cinese, dove "
        "solo la famiglia imperiale e l'alta nobiltà potevano possederne uno. I "
        "cani erano allevati come piccoli compagni simili a leoni e portati "
        "nelle maniche delle vesti di corte. Quando nel 1860 le truppe "
        "britanniche entrarono nella Città Proibita, cinque cani di palazzo "
        "furono portati in Gran Bretagna e uno fu donato alla regina Vittoria. "
        "La razza fu riconosciuta in Gran Bretagna nel 1893 ed è da allora un "
        "compagno molto amato."
    ),
    "pembroke-welsh-corgi": (
        "Il Pembroke Welsh Corgi è un cane da conduzione del Pembrokeshire, in "
        "Galles, dove spingeva il bestiame al pascolo e al mercato mordendo i "
        "garretti. Un'antica leggenda gallese racconta che i cani fossero un "
        "dono delle fate, e i contadini li tennero per secoli come robusti cani "
        "da lavoro di bassa statura. Le due razze gallesi di corgi furono "
        "separate nel 1934 e il Pembroke ottenne il riconoscimento "
        "internazionale. La regina Elisabetta II tenne dei Pembroke per decenni, "
        "rendendo la razza famosa in tutto il mondo."
    ),
    "pomeranian": (
        "Il Pomerania prende il nome dalla Pomerania, la regione sulla costa "
        "baltica tra Germania e Polonia, dove si tenevano grandi spitz bianchi "
        "come cani da pastore e da slitta. Nell'Ottocento gli allevatori europei "
        "e britannici resero il cane sempre più piccolo e ornamentale. Il piccolo "
        "Pomerania della regina Vittoria, che lei portò dall'Italia, è spesso "
        "considerato la causa della moda per la taglia miniaturizzata. La razza "
        "fu riconosciuta in Gran Bretagna nel 1870 ed è oggi uno dei cani da "
        "compagnia più piccoli al mondo."
    ),
    "poodle": (
        "Il Barbone discende da antichi cani d'acqua europei, e il suo nome "
        "deriva dal tedesco pudeln, che indica lo sguazzare nell'acqua. Lavorava "
        "come retriever in Germania e in seguito divenne cane da circo e da "
        "compagnia in Francia, dove è diventato la razza nazionale. La "
        "caratteristica tosatura a leone era in origine pratica: petto e "
        "articolazioni restavano coperti per tenere il cane caldo nell'acqua "
        "fredda. La razza fu standardizzata in Germania nel 1904 ed è oggi "
        "allevata in tre taglie: grande, media e toy."
    ),
    "portuguese-podengo": (
        "Il Podengo Portoghese è un'antica razza da caccia iberica, e cani di "
        "questo tipo erano già descritti in Portogallo nel Medioevo. È allevato "
        "in tre taglie: il piccolo caccia il coniglio in muta, mentre il grande "
        "era usato per cervi e cinghiali. Questi cani viaggiavano con i "
        "navigatori portoghesi nei loro viaggi. La razza fu standardizzata in "
        "Portogallo nel 1955 e resta un robusto cane da lavoro e un vivace "
        "compagno."
    ),
    "pug": (
        "Il Carlino viene dalla Cina, dove cani dal muso corto e piatto erano "
        "tenuti dagli imperatori e commerciati lungo la Via della Seta. I "
        "mercanti olandesi e portoghesi li portarono in Europa nel Cinquecento, e "
        "la razza divenne il favorito della corte olandese: si dice che un "
        "carlino avvertì Guglielmo d'Orange di un attacco spagnolo. In "
        "Inghilterra nell'Ottocento il Carlino fu allevato più piccolo e fu "
        "riconosciuto nel 1885. Oggi è una delle razze toy più conosciute al "
        "mondo."
    ),
    "puli": (
        "Il Puli è un cane da pastore ungherese di origine centroasiatica, "
        "portato nel bacino dei Carpazi dai Magiari più di mille anni fa. Il suo "
        "pelo a corde lo protegge dal maltempo e dai denti delle pecore che "
        "conduce, e lavora in modo veloce e saltellante. Nel Novecento la razza "
        "si perse quasi del tutto e fu ricostruita in Ungheria dagli anni Venti. "
        "Un Puli ungherese partecipò alla ricerca da cui è nato il moderno "
        "addestramento con il clicker."
    ),
    "rat-terrier": (
        "Il Rat Terrier è un cane da fattoria americano dei primi del Novecento, "
        "creato da terrier, feist e altri piccoli cani da caccia portati dai "
        "coloni. Si guadagnò il nome liberando fienili e granai dai ratti, e "
        "lavorava anche su scoiattoli e conigli e come cane da guardia. La razza "
        "fu popolare negli anni Venti e Trenta, poi declinò finché gli "
        "allevatori non la riportarono negli anni Novanta. È un cane da lavoro e "
        "da famiglia robusto e poco esigente."
    ),
    "romagna-water-dog": (
        "Il Lagotto Romagnolo viene dalle pianure della Romagna, nel nord-est "
        "d'Italia, dove per secoli è stato usato per stanare gli uccelli "
        "acquatici dalle paludi. Quando nel Novecento le paludi furono prosciugate, "
        "i cani trovarono un nuovo lavoro: la ricerca dei tartufi, che "
        "individuano esclusivamente con l'olfatto. La razza fu riconosciuta in "
        "Italia nel 1991 e a livello internazionale nel 2005. È l'unica razza "
        "canina tradizionalmente impiegata nella ricerca dei tartufi."
    ),
    "rottweiler": (
        "Il Rottweiler discende dai cani da mandria romani che custodivano e "
        "conducevano il bestiame per le legioni, e alcuni di essi rimasero nella "
        "città tedesca di Rottweil. Lì divennero i cani dei macellai: portavano "
        "il bestiame al mercato e trainavano carri carichi di carne, con il "
        "denaro legato al collare. Quando le ferrovie e il divieto di condurre il "
        "bestiame posero fine a quel lavoro, la razza rischiò di sparire e nel "
        "1901 fu fondato un club per salvarla. Fu riconosciuto in Germania nel "
        "1901 e divenne un famoso cane da polizia, da servizio e da guardia."
    ),
    "saint-bernard": (
        "Il San Bernardo prende il nome dall'ospizio fondato nell'XI secolo da "
        "Bernardo di Mentone in alta quota nelle Alpi svizzere. I monaci "
        "tenevano grandi cani di montagna per sorvegliare il passo e dal "
        "Seicento li usarono per ritrovare i viaggiatori perduti nella neve. Il "
        "più famoso, Barry, avrebbe salvato più di quaranta persone, e ancora "
        "oggi la razza è associata al leggendario barilotto di brandy. Fu "
        "standardizzato in Svizzera nel 1884 ed è il cane nazionale del Paese."
    ),
    "samoyed": (
        "Il Samoiedo prende il nome dai popoli samoiedi della Siberia, che "
        "allevavano spitz bianchi e sorridenti per custodire le renne, trainare "
        "le slitte e sorvegliare l'accampamento. I cani vivevano a stretto "
        "contatto con le famiglie e dormivano persino nelle tende, ed è per "
        "questo che la razza è così legata all'uomo. Alla fine dell'Ottocento "
        "gli esploratori li portarono fuori dalla Siberia, e il primo standard "
        "fu scritto in Gran Bretagna nel 1909. I samoiedi parteciparono a "
        "diverse spedizioni polari, tra cui il tentativo antartico di Scott."
    ),
    "scottish-terrier": (
        "Lo Scottish Terrier proviene dalle Highlands e dalle isole della "
        "Scozia, dove diversi tipi di terrier bassi lavoravano tra i cumuli di "
        "pietre e nelle tane. Nell'Ottocento furono separati, e l'Aberdeen "
        "Terrier divenne lo Scottish Terrier che conosciamo. Il primo standard "
        "fu pubblicato nel 1880 e la razza fu riconosciuta in Gran Bretagna nel "
        "1882. Il suo carattere robusto e la sagoma famosa ne fecero un simbolo "
        "della Scozia e il favorito di presidenti e scrittori."
    ),
    "shar-pei": (
        "Lo Shar Pei è un'antica razza cinese della provincia meridionale del "
        "Guangdong, dove cani dalla pelle rugosa e dalla lingua blu-nera erano "
        "tenuti per la caccia, la conduzione del bestiame e la guardia. Dopo la "
        "rivoluzione cinese la razza quasi scomparve, e negli anni Settanta ne "
        "restavano pochi esemplari tra Hong Kong e Macao. Gli allevatori la "
        "salvarono con l'aiuto dell'Hong Kong Kennel Club, e nel 1991 lo Shar "
        "Pei fu riconosciuto negli Stati Uniti. Oggi è tenuto soprattutto come "
        "cane da compagnia."
    ),
    "shih-tzu": (
        "Lo Shih Tzu fu allevato nei palazzi cinesi ed è spesso legato alla "
        "tradizione buddhista, in cui un piccolo cane simile a un leone era "
        "simbolo di protezione. Gli allevatori di corte incrociarono cani "
        "tibetani con pechinesi per creare la razza che conosciamo, e per secoli "
        "imperatori e nobili tennero questi cani. Negli anni Venti e Trenta "
        "alcuni esemplari arrivarono in Gran Bretagna, dove la razza fu "
        "riconosciuta nel 1946. Il suo nome significa piccolo leone."
    ),
    "siberian-husky": (
        "Il Siberian Husky fu allevato dal popolo ciukcio nel nord-est della "
        "Siberia per trainare slitte leggere su distanze enormi con poco cibo. I "
        "cani vivevano con le famiglie ed erano apprezzati per la resistenza, il "
        "carattere amichevole e il fitto doppio mantello. Nel 1909 arrivarono in "
        "Alaska per le gare con i slitte e nel 1925 le squadre di husky "
        "portarono il siero antidifterico a Nome. La razza fu riconosciuta negli "
        "Stati Uniti nel 1930 ed è oggi un popolare cane da compagnia e da "
        "sport."
    ),
    "sloughi": (
        "Lo Sloughi è un levriero del Maghreb, tenuto da Berberi e Beduini in "
        "Marocco, Algeria, Tunisia e Libia. Caccia lepri, gazzelle e cinghiali "
        "in terreno aperto e vive a stretto contatto con la famiglia, "
        "sorvegliando l'accampamento di notte. La razza è citata nella poesia "
        "araba e arrivò in Europa nell'Ottocento. Un club francese fu fondato nel "
        "1927 e lo Sloughi fu riconosciuto a livello internazionale nel 1935."
    ),
    "treeing-walker-coonhound": (
        "Il Treeing Walker Coonhound fu sviluppato negli Stati Uniti dai segugi "
        "della Virginia portati a ovest dai coloni, in particolare dai cani "
        "Walker del Kentucky. I cacciatori volevano un segugio veloce e dal fiuto "
        "fine, capace di seguire la traccia del procione e dell'orso e poi di "
        "abbaiare sotto l'albero. La razza fu registrata con il proprio nome nel "
        "1945 ed è uno dei coonhound più diffusi in America. Resta soprattutto "
        "un cane da caccia, dolce in casa."
    ),
    "weimaraner": (
        "Il Weimaraner proviene dalla corte di Weimar in Germania, dove "
        "nell'Ottocento i nobili allevarono un cane da caccia versatile per la "
        "selvaggina grossa, il volatile e il lavoro in acqua. Gli allevatori "
        "tedeschi tenevano la razza sotto stretto controllo: prima di vendere un "
        "cucciolo, questo doveva superare le prove di campo e i genitori dovevano "
        "essersi dimostrati al lavoro. Il primo club nacque nel 1897 e nel 1929 "
        "la razza arrivò negli Stati Uniti. Il fantasma grigio dal pelo vellutato "
        "divenne un cane da caccia e da compagnia inconfondibile."
    ),
    "whippet": (
        "Il Whippet proviene dal nord dell'Inghilterra, dove nell'Ottocento i "
        "minatori allevarono un levriero piccolo e tranquillo da tenere in una "
        "casa modesta e da far correre su un rettilineo dopo il turno. Nacque da "
        "greyhound e terrier e veniva usato per inseguire i conigli, attività "
        "chiamata snap-dog. I club di corsa sorsero negli anni Novanta "
        "dell'Ottocento e la razza fu riconosciuta in Gran Bretagna nel 1891. È "
        "il cane più veloce della sua taglia e uno dei più tranquilli in casa."
    ),
    "wire-fox-terrier": (
        "Il Fox Terrier a pelo duro è un terrier britannico delle zone di caccia "
        "alla volpe in Inghilterra, dove il suo compito era stanare la volpe "
        "dalla tana perché i cani potessero proseguire l'inseguimento. Le due "
        "varietà, a pelo liscio e a pelo duro, furono separate da club fondati "
        "nel 1876, e quella a pelo duro divenne la più popolare. Fu riconosciuto "
        "in Gran Bretagna nel 1877 e divenne presto un cane da esposizione di "
        "primo piano, con più titoli Best in Show a Crufts di qualsiasi altra "
        "razza."
    ),
    "xoloitzcuintli": (
        "Lo Xoloitzcuintli, o cane nudo messicano, è una delle razze più antiche "
        "delle Americhe: cani senza pelo erano tenuti in Messico da più di "
        "tremila anni. Gli Aztechi li chiamarono come il dio Xolotl e credevano "
        "che guidassero le anime; servivano anche come guaritori e compagni. Nel "
        "Novecento la razza quasi scomparve e fu salvata dagli allevatori "
        "messicani dagli anni Cinquanta. Il Messico la riconobbe nel 1956, e oggi "
        "è allevata in tre taglie, nuda e con pelo."
    ),
    "yakutian-laika": (
        "La Jakutian Laika è un'antica razza aborigena della Repubblica di "
        "Sakha, in Siberia, dove lavorava in uno dei luoghi abitati più freddi "
        "della terra. I cani trainavano slitte, cacciavano uccelli acquatici e "
        "soprattutto custodivano le renne, vivendo accanto alle famiglie in un "
        "freddo estremo. In epoca sovietica la razza si perse quasi del tutto e "
        "gli allevatori russi iniziarono a ricostruirla negli anni Novanta. Fu "
        "riconosciuta in Russia nel 2005 e a livello internazionale nel 2019, e "
        "fuori dalla Siberia resta rara."
    ),
    "yorkshire-terrier": (
        "Lo Yorkshire Terrier nacque nel nord dell'Inghilterra nell'Ottocento, "
        "quando i tessitori scozzesi si trasferirono nello Yorkshire con i loro "
        "piccoli terrier. Gli operai li incrociarono con i terrier locali per "
        "ottenere un minuscolo cacciatore di ratti per fabbriche e miniere, e "
        "fino al 1870 la razza fu esposta come Broken-Haired Scotch Terrier. Fu "
        "riconosciuta in Gran Bretagna nel 1886 e divenne presto un compagno "
        "alla moda. Oggi è una delle razze più piccole del mondo e un popolare "
        "cane da grembo."
    ),
    "brussels-griffon": (
        "Il Griffone di Bruxelles viene dal Belgio, dove nell'Ottocento i "
        "cocchieri tenevano piccoli cani a pelo ruvido nelle scuderie per "
        "cacciare i ratti e avvertire dell'arrivo di estranei. La razza fu "
        "costruita dal Griffon d'Écurie, dal cane di strada belga e dal piccolo "
        "Carlino, che le diede il muso corto e l'espressione quasi umana. Si "
        "svilupparono due tipi di pelo, e quello liscio oggi si chiama Petit "
        "Brabançon. Il Belgio riconobbe la razza nel 1904, e il film Qualcosa è "
        "cambiato la rese famosa nel mondo."
    ),
    # <<< END IT >>>
}

HISTORY_SR = {
    "afghan-hound": (
        "Afganistanski hrt je jedan od najstarijih tipova hrta: crteži i zapisi "
        "pokazuju da su psi ovog oblika živeli u Avganistanu i okolnim planinama "
        "još pre više hiljada godina. Lokalni lovci koristili su ih za poteru "
        "zečeva i gazela po kamenitom i neravnom terenu, gde brzina sama nije "
        "bila dovoljna. Britanski oficiri doneli su rasu kući krajem XIX veka, a "
        "prvi afganistanci prikazani su u Britaniji 1907. godine. Kennel klub je "
        "priznao rasu 1926, a njen aristokratski izgled učinio ju je modnom "
        "ikonom šezdesetih i sedamdesetih godina."
    ),
    "airedale-terrier": (
        "Erdel terijer potiče iz doline reke Aire u Jorkširu, gde su radnici u "
        "XIX veku ukrstili danas izumrlog staroengleskog crno-tan terijera sa "
        "otterhaundom. Cilj je bio pas koji lovi vidre i pacove, radi ispred "
        "puške i čuva dvorište. Nazvali su ga kraljem terijera, a u Prvom "
        "svetskom ratu britanski vojnici koristili su ga kao kurira i stražara. "
        "Rasa je priznata u Britaniji 1886, a kasnije se proširila kao porodični "
        "pas i policijski radnik."
    ),
    "akita": (
        "Akita se u severnom Japanu gaji vekovima i vezana je za planinske "
        "predele prefekture Akita, gde je korišćena za lov na medvede, divlje "
        "svinje i jelene. U japanskoj tradiciji ova rasa je simbol zdravlja i "
        "sreće, a male statue i danas poklanjaju dragima. Posle Drugog svetskog "
        "rata rasa je skoro nestala i obnovljena je iz malobrojnih preživelih "
        "linija. Najpoznatija akita, Hačiko, čekao je svog vlasnika na tokijskoj "
        "stanici skoro deset godina i danas ima spomenik."
    ),
    "alaskan-malamute": (
        "Aljaski malamut dobio je ime po inuitima Malemut sa Aljaske, koji su "
        "držali teške vučne pse mnogo pre dolaska Evropljana. Ti psi vukli su "
        "sanke natovarene mesom, kožama i opremom, a početkom XX veka radili su i "
        "u polarnim ekspedicijama. Tokom zlatne groznice na Klondajku rasa je "
        "ukrštana sa manjim i bržim vučnim psima i skoro je izgubila prvobitni "
        "tip. Dvadesetih i tridesetih godina XX veka odgajivači su vratili "
        "teškog i snažnog malamuta, a 1935. rasa je priznata u SAD."
    ),
    "american-cocker-spaniel": (
        "Američki koker španijel potiče od pasa koji su u XIX veku iz Engleske "
        "stigli u Severnu Ameriku, kada je koker još bio jedna rasa sa engleskim "
        "kokerom. Američki odgajivači želeli su manjeg psa svilene dlake za lov "
        "na šljuku u gustom rastinju. Tipovi su se razišli, a 1946. američki "
        "koker priznat je kao samostalna rasa. Tokom XX veka postao je jedan od "
        "najpopularnijih pratilaca i uzor za Diznijevu Ledi."
    ),
    "american-eskimo-dog": (
        "Američki eskimski pas potiče od belih špica koje su nemački "
        "imigranti doneli u SAD u XIX veku. Nastupali su u putujućim cirkusima, "
        "pa je mali beli pas zbog svojih trikova postao poznat u celoj zemlji. "
        "Kada su antinemačka osećanja porasla tokom Prvog svetskog rata, ime je "
        "promenjeno iz nemački špic u američki eskimski pas. Rasa je priznata u "
        "SAD 1995, a i danas je cenjena kao živahan porodični pas i čuvar."
    ),
    "american-staffordshire-terrier": (
        "Američki stafordski terijer potiče od bul-end-terijera koji su u XIX "
        "veku iz Britanije stigli u SAD. Američki odgajivači stvorili su višeg i "
        "težeg psa od engleskog originala i koristili su ga na farmi, u "
        "porodici i u borbi. Najpre je registrovan kao američki bul terijer, a "
        "zatim kao stafordski terijer. Ime američki stafordski terijer "
        "usvojeno je 1969. da bi se razlikovao od engleskog stafordskog "
        "bulterijera, a rasa je postala popularan porodični pas."
    ),
    "anatolian-shepherd-dog": (
        "Anatolijski pastir drevni je čuvar stoke sa visoravni Anatolije u "
        "Turskoj. Vekovima je živeo sa pastirima i njihovim stadima, čuvajući "
        "ovce od vukova i medveda, ali ih nije gonio. Psi su birani po "
        "izdržljivosti, samostalnosti i sposobnosti da rade sami u surovoj "
        "klimi. Sedamdesetih godina XX veka Turska je počela da evidentira rasu, "
        "koja se proširila Evropom i SAD kao radni čuvar i miran, impozantan "
        "porodični pas."
    ),
    "australian-shepherd": (
        "Australijski ovčar razvijen je na zapadu SAD, a ne u Australiji, iako "
        "su mu preci bili baskijski i australijski pastirski psi. Rančeri su "
        "tražili psa koji može da goni ovce i goveda na velike daljine i radi "
        "po vrućini, prašini i snegu. Rasu su držale radničke porodice i rodeo "
        "izvođači, a ime je dobila po stoci i pastirima koji su stizali sa "
        "australijskim brodovima. Priznata je u SAD 1991. i danas je jedna od "
        "najpoznatijih pastirskih rasa."
    ),
    "azawakh": (
        "Azavak je hrt Sahela, koji su odgajili Tuarezi i drugi nomadski narodi "
        "Malija, Nigera i Burkine Faso. Lovi gazele i zečeve po otvorenoj "
        "pustinji i čuva logor, živeći blizu ljudi. Rasa je dobila ime po "
        "dolini Azavak, a njeno mršavo telo prilagođeno je vrućini i dugim "
        "putevima. Prvi azavaci stigli su u Evropu sedamdesetih godina XX veka, "
        "a međunarodno priznanje rasa je dobila 1981. godine."
    ),
    "barbado-da-terceira": (
        "Barbado da Terseira potiče sa ostrva Terseira na Azorima, gde je "
        "odgajan za rad sa govedima na grubom vulkanskom zemljištu. Ostrvskim "
        "farmerima bio je potreban pas srednje veličine koji čuva stoku, čuva "
        "imanje i blag je prema porodici. Van Azora rasa je vekovima bila skoro "
        "nepoznata, a spasli su je lokalni odgajivači u XX veku. Portugal je "
        "priznao rasu 2004; danas je retka, ali sve češća pastirska i porodična "
        "rasa."
    ),
    "basset-hound": (
        "Baset haund potiče od francuskih goniča koje su držali manastiri i "
        "plemićke kuće za lov na zečeve i jelene. Nizak i spor tip pojavio se u "
        "Francuskoj u XVI veku i usavršen je u XIX, kada su lovci želeli psa "
        "koga mogu da prate peške. Britanski odgajivači uvezli su rasu 1866. i "
        "dali joj današnji izgled. Priznata je u Britaniji 1880, a u XX veku "
        "postala je poznat reklamni i porodični pas."
    ),
    "bedlington-terrier": (
        "Bedlington terijer razvijen je u rudarskom kraju Nortamberlenda i "
        "dobio je ime po gradu Bedlingtonu. Rudari i krivolovci koristili su ga "
        "za lov na pacove, zečeve i vidre, a mogao je da se provuče kroz uske "
        "jame. Njegova jagnjeća dlaka i povijen leđni deo kriju žilavog "
        "terijera, a nekada se zvao Rotberi terijer. Priznat je u Britaniji "
        "1877, a kasnije je postao izložbeni i porodični pas."
    ),
    "bichon-frise": (
        "Bišon frize potiče od malih belih pasa koje su mornari i trgovci u "
        "srednjem veku nosili po Sredozemlju. Tip je usavršen u Francuskoj, gde "
        "je bišon postao miljenik dvora, a kasnije uličnih izvođača i "
        "orguljaša. Gusta kovrdžava dlaka i vesela narav učinile su ga "
        "popularnim cirkuskim psom. U Francuskoj je rasa priznata 1933, u SAD "
        "1972, a danas je veoma voljen pratilac."
    ),
    "black-and-tan-coonhound": (
        "Crno-tan kunhaund razvijen je u SAD od evropskih goniča koje su "
        "doneli kolonisti, pre svega od Talbot haunda i bladhaunda. Lovcima je "
        "bio potreban pas koji noću može da prati trag rakuna ili medveda i "
        "zatim da laje pod drvetom. Rasa radi isključivo nosom i poznata je po "
        "dubokom, ravnomernom glasu na tragu. Priznata je u SAD 1945. i ostaje "
        "specijalizovan lovački pas."
    ),
    "bloodhound": (
        "Bladhaund je jedan od najstarijih goniča: njegovi preci opisani su u "
        "Evropi još u VII veku, a tip su usavršili monasi u Belgiji i "
        "Francuskoj. Ime se odnosi na čistokrvni, plemeniti soj, a ne na krv. "
        "Vekovima je korišćen za praćenje traga jelena, divljih svinja i kasnije "
        "ljudi, a njegovi rezultati prihvatani su i na sudu. Rasa je "
        "standardizovana u Britaniji 1897. i i danas je merilo za rad na tragu."
    ),
    "bolognese": (
        "Bolonjez je mali beli pas pratilac iz italijanske Bolonje, a njegovi "
        "preci pojavljuju se na slikama iz renesanse. Plemićke porodice držale "
        "su ih kao pse za krilo i poklanjale drugim evropskim dvorovima kao "
        "diplomatski dar. U XIX veku rasa je skoro nestala i obnovljena je iz "
        "malobrojnih preživelih linija u XX veku. U Italiji je bolonjez priznat "
        "1956, a van domovine je i danas redak."
    ),
    "border-collie": (
        "Border koli nastao je na granici Engleske i Škotske, gde je pastirima "
        "bio potreban pas koji stado na brdima vodi na jednu komandu ili "
        "zvižduk. Odgajalo se na inteligenciju, izdržljivost i pre svega na tihi "
        "kontrolišući pogled koji je nazvan eye. Ime se ustalilo 1915; pre toga "
        "psi su se zvali jednostavno radni koli. Rasa je i danas merilo u "
        "takmičenjima u čuvanju stada, a jedan njen predstavnik, Čejser, naučio "
        "je imena više od hiljadu igračaka."
    ),
    "border-terrier": (
        "Border terijer potiče sa Čeviotskih brda na granici Engleske i "
        "Škotske, gde je radio sa fokshaundima i lovio lisice koje su ugrožavale "
        "ovce. Morao je biti dovoljno uzak da uđe za lisicom u jamu i dovoljno "
        "žilav da ceo dan prati konje. Prvo je prikazivan kao koketdejlski "
        "terijer, a ime border dobio je 1880. U Britaniji je priznat 1920. i i "
        "danas je radni terijer i čvrst porodični pas."
    ),
    "borzoi": (
        "Ruski hrt stvorilo je rusko plemstvo ukrštajući arapske i persijske "
        "hrte sa lokalnim dugodlakim lovačkim psima. Korišćen je u lovu na "
        "vukove, radeći u paru ili manjim čoporima zajedno sa lovcima na "
        "konjima. Rasu je držalo gotovo isključivo plemstvo, a revolucija 1917. "
        "skoro ju je uništila. Preživeli psi izvezeni su dvadesetih godina XX "
        "veka, a tokom tog veka rasa se afirmisala kao elegantan izložbeni i "
        "porodični pas."
    ),
    "boxer": (
        "Bokser je razvijen u Nemačkoj u XIX veku od bulenajsera i engleskog "
        "buldoga. Minhenski odgajivači želeli su snažnog čuvara i psa za "
        "čuvanje stoke, kratke i čiste glave i mirne naravi. Prvi bokser "
        "registrovan je 1904, a rasa se brzo proširila kao policijski i vojni "
        "pas. U Prvom svetskom ratu bokser je služio kao kurir i stražar, a "
        "posle rata postao je jedan od najpopularnijih porodičnih pasa u Evropi "
        "i Severnoj Americi."
    ),
    "bulldog": (
        "Engleski buldog potiče od starih pasa mastifskog tipa koji su korišćeni "
        "za borbu s bikovima, surovu zabavu zabranjenu u Britaniji 1835. godine. "
        "Kada je ta zabava prestala, odgajivači su od psa napravili blagog "
        "pratioca i dali mu težak oblik kratke glave kakav danas poznajemo. Prvi "
        "klub rase osnovan je 1875, a buldog je postao nacionalni simbol "
        "Britanije — u karikaturama su ga poredili sa karakterom same zemlje. "
        "Savremeno odgajivanje usmereno je na zdravlje, disanje i pokretljivost."
    ),
    "bull-terrier": (
        "Bul terijer nastao je u Engleskoj XIX veka ukrštanjem starog "
        "bul-end-terijera sa danas izumrlim belim engleskim terijerom. Džejms "
        "Hinks želeo je potpuno belog, atletskog psa jajolike glave, a rasa je "
        "priznata u Britaniji 1887. Obojeni psi dodati su u XX veku i "
        "registrovani kao stafordski bulterijeri. Bul terijer postao je poznat "
        "kao sportski i vojni maskota, a kasnije kao stilizovan gradski "
        "pratilac."
    ),
    "cane-corso": (
        "Kane korso potiče iz južne Italije i vodi poreklo od starih rimskih "
        "molosa koji su korišćeni za čuvanje, lov i rat. Ime mu potiče od "
        "latinske reči za telesnog čuvara, a vekovima je radio na farmama, "
        "čuvao stoku i štitio imanja. Posle Drugog svetskog rata rasa je skoro "
        "nestala i spasli su je italijanski ljubitelji sedamdesetih godina. "
        "Italija je 1987. donela standard, a danas je kane korso popularan "
        "čuvar i porodični pas širom sveta."
    ),
    "catahoula-leopard-dog": (
        "Katahula je zvanični pas države Luizijane i nosi ime po parohiji "
        "Katahula. Nastala je od pasa španskih istraživača, francuskih "
        "naseljenika i indijanskih pasa, a njen pegavo, leopardasto krzno "
        "jedinstven je među radnim rasama. Njome su čuvane divlje svinje i "
        "goveda u močvarama i borovim šumama, često u čoporima. Zvanično je "
        "priznata u SAD 1979. i i danas je pre svega radni pas."
    ),
    "cavalier-king-charles-spaniel": (
        "Kavalir king Čarls španijel oživljava male sobne španijele koje su na "
        "slikama XVI i XVII veka stajale pored evropskog plemstva. Kralj Čarls "
        "II toliko ih je voleo da je tip dobio njegovo ime. Do XX veka stari "
        "izgled potisnuo je engleski toj španijel ravnog lica, a američki "
        "odgajivači raspisali su nagradu za pse sa dugom njuškom kao na starim "
        "slikama. U Britaniji je kavalir priznat 1945. i od tada je jedna od "
        "najpopularnijih pratilačkih rasa."
    ),
    "collie-rough": (
        "Dugodlaki koli je škotski pastirski pas iz Visoravni, gde je radio sa "
        "ovcama po svakom vremenu. Rasa je usavršena u XIX veku, a naklonost "
        "kraljice Viktorije prema ovim psima učinila ih je modernim i van "
        "Škotske. Ime potiče od stare škotske reči za korisnog crno-belog "
        "ovčarskog psa. U Britaniji je rasa priznata 1874, a romani i filmovi o "
        "Lasi učinili su kolija svetskim simbolom vernog porodičnog psa."
    ),
    "czechoslovakian-wolfdog": (
        "Čehoslovački vučjak nastao je 1955. kao vojni eksperiment u "
        "Čehoslovačkoj, ukrštanjem nemačkog ovčara sa karpatskim vukom. Cilj je "
        "bio da se poslušnost ovčara spoji sa izdržljivošću i čulima vuka za "
        "službu na granici. Ukrštanje je uspelo, ali psi su se pokazali teški "
        "za obuku i vojska ih nikada nije koristila u velikom broju. Rasa je "
        "priznata u Čehoslovačkoj 1982, a međunarodno 1999; danas je zahtevan "
        "radni i porodični pas."
    ),
    "dachshund": (
        "Jazavičar je u Nemačkoj razvijan vekovima od niskih lovačkih pasa koji "
        "su mogli da prate jazavce i lisice u njihovim jamama. Ime znači pas za "
        "jazavce, a u nemačkim zapisima rasa se pominje od XV veka. Odgajena su "
        "tri tipa dlake i dve veličine za različitu divljač, a psi su radili i "
        "u čoporima na divljim svinjama i jelenima. U Britaniji je priznat 1881. "
        "i postao je veoma voljen porodični pas — dug, nizak i vrlo privržen."
    ),
    "dalmatian": (
        "Dalmatinac je dobio ime po jadranskoj regiji Dalmaciji, a psi ovog "
        "pegavog tipa pojavljuju se na slikama i u crkvenim zapisima iz XVII i "
        "XVIII veka. Rasa je korišćena kao pas za kočije: trčao je pored ili pod "
        "osovinom, čistio put i čuvao konje u gostionicama. Britanski "
        "odgajivači standardizovali su ga u XIX veku, a priznat je 1888. Veza "
        "sa vatrogascima počela je kada su se uz konjske vatrogasne zaprege "
        "držali dalmatinci da bi smirivali konje."
    ),
    "dobermann": (
        "Doberman je stvorio Karl Fridrih Luis Doberman, nemački poreznik i "
        "hvatač pasa iz Apolda, devedesetih godina XIX veka. Bio mu je potreban "
        "neustrašiv i inteligentan čuvar koji ga prati u opasnim obilascima, pa "
        "je rasu stvorio od nekoliko čuvarskih i lovačkih tipova. Prvi klub "
        "osnovan je 1899, a pas se brzo proširio kao policijski i vojni. "
        "Početkom XX veka rasa je međunarodno priznata i i danas je jedan od "
        "najcenjenijih službenih i zaštitnih pasa."
    ),
    "drever": (
        "Drever je švedski gonič nastao od vestfalske jazavčarke i drugih "
        "nemačkih lovačkih pasa koji su u XIX veku stigli na sever. Švedski "
        "lovci želeli su niskog, mirnog goniča koji prati srneću i zečju "
        "tragu kroz sneg i gustu šumu tempom kojim čovek može da ide. Godinama "
        "se zvao švedska jazavčarka, a ime drever dobio je 1947. U Švedskoj "
        "je nacionalno priznat i jedan je od najpopularnijih lovačkih pasa te "
        "zemlje."
    ),
    "dutch-shepherd-dog": (
        "Holandski ovčar je pastirska rasa Holandije, odgajana u tri tipa dlake: "
        "kratkoj, dugoj i oštroj. Farmeri su ih držali da čuvaju ovce i stoku, "
        "čuvaju dvorište i vuku mala kola, a koristili su ih i kao policijske i "
        "kurirske pse. Rasa je standardizovana 1898. uz osnivanje holandskog "
        "kluba, a posle Drugog svetskog rata broj pasa je naglo opao. Ozbiljno "
        "odgajivanje nastavljeno je sedamdesetih godina, a danas rasa radi u "
        "policiji i službama traganja."
    ),
    "english-setter": (
        "Engleski seter razvijan je u Britaniji više od četiri stotine godina od "
        "pasa koji su se spuštali pred divljači i time omogućavali lovcu da baci "
        "mrežu na ptice. U XIX veku Edvard Laverak i Persel Levelin stvorili su "
        "dve linije od kojih potiče skoro svaki savremeni seter. Rasa je "
        "priznata u Britaniji 1874. Poznata je po blagoj naravi i pegavom "
        "belton krznu, a i danas radi kao ptičar i živi kao porodični pas."
    ),
    "french-bulldog": (
        "Francuski buldog počeo je kao mali engleski buldog koji su držale "
        "čipkarice iz Notingema i koji su šezdesetih godina XIX veka ponele sa "
        "sobom u Francusku. U Parizu su ti psi postali miljenici društva i "
        "umetnika, a francuski odgajivači birali su uspravne slepi miš uši i "
        "kompaktno telo. Rasa je priznata u Francuskoj i u SAD 1898. Posle pada "
        "popularnosti početkom XX veka, danas je jedan od najčešćih pratilaca u "
        "svetu."
    ),
    "german-shepherd-dog": (
        "Nemački ovčar osnovao je Maks fon Štefanic 1899, želeći radnog i "
        "pastirskog psa velike inteligencije i izdržljivosti. Kupio je psa "
        "Hektora, preimenovao ga u Horand fon Grafrat i sa klubom SV dokazao "
        "vrednost rase u službi. Pas se brzo proširio kao policijski, vojni i "
        "pas vodič slepih i postao poznat u oba svetska rata. Početkom XX veka "
        "rasa je međunarodno priznata i ostaje jedna od najkorišćenijih radnih "
        "rasa."
    ),
    "german-shorthaired-pointer": (
        "Nemački kratkodlaki ptičar potiče iz Nemačke XIX veka, gde je lovcu "
        "bio potreban jedan pas za sve: markiranje, donošenje, tragu i rad u "
        "vodi. Rasa je stvorena od starih nemačkih ptičara, goniča i vodenih "
        "pasa, a razvojem je rukovodio princ Albreht cu Solms-Braunfels. Prva "
        "rodovska knjiga objavljena je 1872. U SAD je priznat 1930. i danas je "
        "jedan od najsvestranijih lovačkih pasa na svetu."
    ),
    "german-spitz": (
        "Nemački špic pripada najstarijoj porodici pasa srednje Evrope, tipu "
        "špica koji je vekovima držan uz kuće i farme. Rasa se po veličini deli "
        "na vučjeg špica, velikog, srednjeg, malog i pomeranca, a sve ih "
        "povezuju uspravne uši, gusta dlaka i uvrnut rep. Špici su radili kao "
        "čuvari, pastiri i pratioci, a njihov lik pojavljuje se u nemačkoj "
        "umetnosti srednjeg veka. Rasa je standardizovana u Nemačkoj 1899. i "
        "međunarodno priznata u XX veku."
    ),
    "golden-retriever": (
        "Zlatni retriver stvoren je u škotskoj visoravni u drugoj polovini XIX "
        "veka, a tvorac mu je Dadli Marjoribanks, kasniji lord Tvidmut. Ukrstio "
        "je žutog retrivera talasaste dlake sa danas izumrlim tvid vodenim "
        "španijelom, da bi dobio poslušnog psa za donošenje divljači sa zemlje i "
        "iz vode. Prvo leglo rođeno je 1868, a linija je decenijama držana u "
        "tajnosti. Rasa je priznata u Britaniji 1913. i danas je jedan od "
        "najomiljenijih porodičnih pasa, vodiča i spasilaca."
    ),
    "great-dane": (
        "Nemačka doga razvijena je u Nemačkoj od starih mastifa i lovačkih pasa, "
        "a savremeni tip odgajivači su utvrdili krajem XIX veka. Uprkos "
        "engleskom imenu, rasa je nemačka: zvala se Deutsche Dogge, a 1880. "
        "komitet u Berlinu usvojio je prvi standard. Pas je odgajan za lov na "
        "divlje svinje sa konja i za čuvanje imanja, a visina i mirno držanje "
        "doneli su mu nadimak Apolon među psima. Početkom XX veka rasa je "
        "međunarodno priznata."
    ),
    "hovawart": (
        "Hovavart je stari nemački seoski pas čije ime znači čuvar dvorišta, a "
        "psi tog tipa pominju se u nemačkim pravnim spomenicima srednjeg veka. "
        "Savremenu rasu obnovili su dvadesetih godina XX veka odgajivači koji "
        "su u Švarcvaldu i Harcu tražili pse koji odgovaraju starim opisima. "
        "Ukrštani su sa nemačkim ovčarima, njufaundlendima i leonbergerima da "
        "bi se tip učvrstio. Nemačka je priznala hovavarta 1937, a i danas se "
        "drži uglavnom kao radni čuvar i porodični pas."
    ),
    "irish-wolfhound": (
        "Irski vučji hrt drevni je irski hrt kojim su lovljeni vukovi, losovi i "
        "divlje svinje, a pominje se u irskim zapisima i sagama od prvih vekova "
        "nove ere. Irski poglavari poklanjali su te pse evropskim i engleskim "
        "kraljevima, što je rasu i proširilo i kasnije osiromašilo. U XIX veku "
        "vukova više nije bilo i rasa je skoro izumrla; kapetan Džordž Grejam "
        "obnovio ju je od preživelih linija i sličnih hrtova. Priznata je u "
        "Britaniji 1886. i najviša je od svih rasa pasa."
    ),
    "italian-sighthound": (
        "Mali italijanski hrt je mali hrt koji se u italijanskoj umetnosti "
        "pojavljuje od rimskog doba, a držale su ga plemićke porodice širom "
        "poluostrva. Njime su lovljeni zečevi i kunići, a pre svega je bio "
        "elegantan pratilac na dvorovima Firence i Milana. Rasa je "
        "standardizovana u Italiji 1928, a prvi psi stigli su u Britaniju "
        "pedesetih godina. Njegova tanka građa i tiha narav čine ga danas "
        "omiljenim psom za stan."
    ),
    "italian-spinone": (
        "Italijanski spinone je oštrodlaki ptičar iz Pijemonta i Lombardije, "
        "gde je vekovima radio u poljima i močvarama severne Italije. Traži "
        "polako i blizu, markira i donosi divljač i na zemlji i u vodi, a "
        "nekada je korišćen i u lovu sa sokolovima. U Italiji je standard "
        "usvojen 1950, kada je klub počeo da spasava rasu od nestajanja posle "
        "rata. I danas je redak, ali cenjen lovački pas i blag porodični "
        "pratilac."
    ),
    "kai": (
        "Kai je japanski špic srednje veličine iz planina prefekture Jamanaši, "
        "a ime nosi po staroj provinciji Kai. Tamo se vekovima drži za lov na "
        "jelene i divlje svinje po strmim i snežnim predelima. Jedna je od "
        "retkih japanskih rasa sa tigrastim krznom i poznata je po "
        "samostalnosti i okretnosti. Kai je 1934. proglašen spomenikom prirode "
        "u Japanu, a van domovine je i dalje redak."
    ),
    "keeshond-wolfspitz": (
        "Kishond, ili vučji špic, najveća je varijanta nemačkog špica i stari "
        "brodski pas Holandije. Brodari su držali ove sede pse lisičjeg lica na "
        "svojim plovilima kao čuvare i pratioce na kanalima i rekama. "
        "Holandsko ime rase potiče od Kisa de Gizelara, patriote iz XVIII "
        "veka, čiji je pas postao znak jednog političkog pokreta. Prvi "
        "standard napisan je 1927, a danas se kishond drži uglavnom kao "
        "živahan porodični pratilac."
    ),
    "kleiner-munsterlander": (
        "Mali münsterlender stari je svestrani ptičar iz oblasti Minstera u "
        "Nemačkoj, a ptičari tog tipa pojavljuju se na nemačkim slikama još u "
        "XV veku. Radi ispred puške, markira, donosi i prati trag ranjene "
        "divljači, a koristi se i u lovu sa sokolom. Nemački odgajivači su "
        "1919. odredili dve veličine, a mali münsterlender dobio je svoj klub. "
        "Danas je popularan radni lovački pas u Evropi i uravnotežen porodični "
        "pas."
    ),
    "labrador-retriever": (
        "Labrador retriver ne potiče iz Labradora, već sa Njufaundlenda, gde su "
        "mali vodeni psi radili sa ribarima i vukli mreže kroz ledenu vodu. "
        "Britanci su ih kupovali početkom XIX veka, a lord Malmsberi i drugi "
        "sportisti odgajali su ih za donošenje divljači na zemlji i u vodi. "
        "Kennel klub registrovao je rasu 1903. Decenijama je među "
        "najpopularnijim porodičnim psima sveta i mnogo se koristi kao vodič, "
        "pomoćni i spasilački pas."
    ),
    "nederlandse-kooikerhondje": (
        "Holandski kokerhondje stari je holandski pas španijel tipa, korišćen "
        "na patkarskim lovkama, dugim levkastim zamkama u Holandiji. Pas je "
        "mamio patke duž kanala svojim belim, pernatim repom, a zatim je čekao "
        "u tišini dok čuvar ne zatvori zamku. U XX veku rasa je skoro nestala i "
        "obnovila ju je iz nekoliko pasa baronica van Hardenbruk van Ammerstol "
        "od 1939. Holandija je priznaje od 1971; i danas je redak, ali šarmantan "
        "pratilac."
    ),
    "norwegian-elkhound-grey": (
        "Norveški sivi losov pas drevni je skandinavski špic, pronađen u "
        "grobnicama starim više hiljada godina. Norveški lovci koristili su ga "
        "da pronađe i zadrži losa i medveda lajući uporno, a čuvao je i "
        "dvorišta i čuvao stoku. Rasa je standardizovana u Norveškoj 1901, a "
        "siva varijanta starija je i rasprostranjenija od druge. Početkom XX "
        "veka priznata je međunarodno i cenjena je kao lovački i porodični "
        "pas."
    ),
    "nova-scotia-duck-tolling-retriever": (
        "Novoškotski retriver za mamljenje pataka razvijen je u okrugu Jarmut u "
        "Novoj Škotskoj, gde su lovci primetili da lisice koje se igraju na "
        "obali privlače radoznalu vodenu pticu. Odgajivači su stvorili riđeg "
        "psa koji oponaša to ponašanje: on se prevrće po obali i mami patke na "
        "domet, a zatim donosi odstreljenu divljač. Rasa se generacijama držala "
        "lokalno i priznata je u Kanadi 1945. Najmanji je od retrivera i "
        "zvanični pas Nove Škotske."
    ),
    "old-english-sheepdog": (
        "Staroengleski ovčar potiče iz zapadne Engleske, gde je gonio stoku i "
        "ovce na pijacu na velike daljine, umesto da ih čuva u polju. Gusta "
        "dlaka štitila ga je od vremena i od zuba životinja koje je gonio, a rep "
        "je tradicionalno kupiran kao znak radnog psa. Rasa je standardizovana "
        "u Britaniji 1888. i postala je omiljen izložbeni pas. Njegova blaga, "
        "lakrdijaška narav učinila ga je kasnije porodičnim miljenikom."
    ),
    "otterhound": (
        "Oterhaund je stari britanski gonič, odgajan za lov na vidre koje su "
        "praznile reke i ribnjake. Radi u čoporu, prati trag na zemlji i vidi "
        "plen u vodi, a oštra dlaka i plivaće kožice omogućavaju mu duge sate u "
        "vlazi. Lov na vidre zabranjen je u Britaniji 1978, a rasa je naglo "
        "opala. Priznata je u Britaniji 1910, ali danas u svetu postoji samo "
        "nekoliko stotina pasa — jedna je od najređih britanskih rasa."
    ),
    "pekingese": (
        "Pekingezer je vekovima držan u carskoj palati Kine, gde su ga mogli "
        "imati samo carska porodica i najviše plemstvo. Psi su odgajani kao mali "
        "pratioci nalik lavu i nošeni u rukavima dvorskih haljina. Kada su "
        "britanske trupe 1860. ušle u Zabranjeni grad, pet dvorskih pasa "
        "odvedeno je u Britaniju, a jedan je poklonjen kraljici Viktoriji. Rasa "
        "je priznata u Britaniji 1893. i od tada je omiljen pratilac."
    ),
    "pembroke-welsh-corgi": (
        "Pembroke velški korgi je pas za čuvanje stoke iz Pembrokshira u Velsu, "
        "gde je gonio stoku na pašu i pijacu štipajući je za pete. Stara velška "
        "legenda kaže da su psi dar vila, a farmeri su ih vekovima držali kao "
        "žilave niske radne pse. Dve velške rase korgija razdvojene su 1934, a "
        "pembroke je dobio međunarodno priznanje. Kraljica Elizabeta II držala "
        "je pembroke decenijama, što je rasu učinilo poznatom u celom svetu."
    ),
    "pomeranian": (
        "Pomeranac je dobio ime po Pomeraniji, oblasti na obali Baltika između "
        "Nemačke i Poljske, gde su držani veliki beli špici kao ovčarski i "
        "vučni psi. Odgajivači u Evropi i Britaniji činili su psa tokom XIX "
        "veka sve manjim i ukrasnijim. Mali pomeranac kraljice Viktorije, koji "
        "je donela iz Italije, često se smatra uzrokom mode minijaturnih "
        "veličina. Rasa je priznata u Britaniji 1870. i danas je jedan od "
        "najmanjih pratilaca na svetu."
    ),
    "poodle": (
        "Pudla potiče od starih evropskih vodenih pasa, a njeno ime dolazi od "
        "nemačke reči pudeln, koja označava prskanje u vodi. Radila je kao "
        "retriver u Nemačkoj, a kasnije je u Francuskoj postala cirkuski i "
        "porodični pas, gde je proglašena nacionalnom rasom. Prepoznatljiva "
        "šišanja u obliku lava prvobitno su bila praktična: grudi i zglobovi "
        "ostajali su obrasli da bi pas ostao topao u hladnoj vodi. Rasa je "
        "standardizovana u Nemačkoj 1904. i danas se odgaja u tri veličine: "
        "velika, srednja i patuljasta."
    ),
    "portuguese-podengo": (
        "Portugalski podengo je drevna iberijska lovačka rasa, a psi ovog tipa "
        "opisani su u Portugalu još u srednjem veku. Odgaja se u tri veličine: "
        "mali podengo lovi kuniće u čoporima, a veliki je korišćen za jelene i "
        "divlje svinje. Ti psi su putovali sa portugalskim moreplovcima na "
        "njihovim putovanjima. Rasa je standardizovana u Portugalu 1955. i i "
        "danas je izdržljiv radni gonič i živahan pratilac."
    ),
    "pug": (
        "Mops potiče iz Kine, gde su kratkoglave pse ravnog nosa držali carevi i "
        "prodavali duž Puta svile. Holandski i portugalski trgovci doneli su ih "
        "u Evropu u XVI veku, a rasa je postala miljenik holandskog dvora — "
        "priča kaže da je mops upozorio Viljema Oranskog na španski napad. U "
        "Engleskoj je mops u XIX veku odgajan manji i priznat je 1885. Danas je "
        "jedna od najpoznatijih malih rasa na svetu."
    ),
    "puli": (
        "Puli je mađarski pastirski pas centralnoazijskog porekla, koji su "
        "Mađari doneli u karpatski basen pre više od hiljadu godina. Njegova "
        "dlaka u obliku gajtana štiti ga od vremena i od zuba ovaca koje goni, a "
        "radi brzo i skakutavo. U XX veku rasa je skoro izgubljena, ali je u "
        "Mađarskoj obnovljena od dvadesetih godina. Jedan mađarski puli "
        "učestvovao je u istraživanju iz kojeg je nastao savremeni trening "
        "klikerom."
    ),
    "rat-terrier": (
        "Ret terijer je američki seoski pas s početka XX veka, nastao od "
        "terijera, fajstova i drugih malih lovačkih pasa koje su doneli "
        "kolonisti. Ime je dobio jer je čistio ambare i žitnice od pacova, a "
        "radio je i na vevericama i kunićima i čuvao dvorište. Rasa je bila "
        "popularna dvadesetih i tridesetih godina, potom je oslabila, dok je "
        "odgajivači nisu vratili devedesetih. To je čvrst, nezahtevan radni i "
        "porodični pas."
    ),
    "romagna-water-dog": (
        "Romanski vodeni pas, lagoto romanjolo, potiče iz nizija Romanje u "
        "severozapadnoj Italiji, gde je vekovima korišćen za podizanje vodene "
        "ptice iz močvara. Kada su močvare u XX veku isušene, psi su dobili "
        "novi posao: traženje tartufa, koje pronalaze isključivo nosom. U "
        "Italiji je rasa priznata 1991, a međunarodno 2005. Jedina je rasa "
        "pasa koja se tradicionalno koristi za lov na tartufe."
    ),
    "rottweiler": (
        "Rotvajler potiče od rimskih pastirskih pasa koji su čuvali i gonili "
        "stoku za legije, a deo njih ostao je u nemačkom gradu Rotvajlu. Tamo "
        "su postali mesarski psi: gonili su stoku na pijacu i vukli kola s "
        "mesom, a novac je bio vezan za njihove ogrlice. Kada su železnice i "
        "zabrana gonjenja stoke okončale taj posao, rasa je skoro nestala, pa je "
        "1901. osnovan klub za njeno spašavanje. Iste godine priznata je u "
        "Nemačkoj i postala je svetski poznat policijski, službeni i čuvarski "
        "pas."
    ),
    "saint-bernard": (
        "Bernardinac je dobio ime po hospiciju koji je u XI veku osnovao "
        "Bernard od Mentona visoko u švajcarskim Alpima. Monasi su držali "
        "velike planinske pse za čuvanje prevoja, a od XVII veka koristili su "
        "ih za pronalaženje putnika izgubljenih u snegu. Najpoznatiji od njih, "
        "Bari, navodno je spasao više od četrdeset ljudi, a rasa se i danas "
        "povezuje sa legendarnom buradom brendija. Standardizovan je u "
        "Švajcarskoj 1884; nacionalni je pas te zemlje."
    ),
    "samoyed": (
        "Samojed je dobio ime po samojedskim narodima Sibira, koji su odgajali "
        "bele špiceve nasmejane glave za čuvanje irvasa, vuču sanki i čuvanje "
        "logora. Psi su živeli uz porodice i čak spavali u šatorima, zbog čega "
        "je rasa izuzetno vezana za ljude. Krajem XIX veka istraživači su ih "
        "izveli iz Sibira, a prvi standard napisan je u Britaniji 1909. "
        "Samojedi su učestvovali u nekoliko polarnih ekspedicija, uključujući "
        "Skotov pokušaj na Antarktiku."
    ),
    "scottish-terrier": (
        "Škotski terijer potiče iz Visoravni i sa ostrva Škotske, gde je "
        "nekoliko niskih terijerskih tipova radilo po kamenim jamama. U XIX "
        "veku oni su razdvojeni, a aberdinski terijer postao je škotski "
        "terijer kakvog danas poznajemo. Prvi standard objavljen je 1880, a "
        "1882. rasa je priznata u Britaniji. Njegova čvrsta narav i poznata "
        "silueta učinili su ga simbolom Škotske i miljenikom predsednika i "
        "pisaca."
    ),
    "shar-pei": (
        "Šar pej je drevna kineska rasa iz južne provincije Guangdung, gde su "
        "držani psi opuštene, naborane kože i plavo-crnog jezika za lov, "
        "čuvanje stoke i stražu. Posle kineske revolucije rasa je skoro "
        "nestala, a sedamdesetih godina XX veka ostalo je samo nekoliko pasa u "
        "Hongkongu i Makau. Odgajivači su ih spasli uz pomoć Hongkonškog kennel "
        "kluba, a 1991. šar pej je priznat u SAD. Danas se drži uglavnom kao "
        "pas pratilac."
    ),
    "shih-tzu": (
        "Ši cu je odgajan u kineskim palatama i često se povezuje sa "
        "budističkom tradicijom, u kojoj je mali pas nalik lavu bio simbol "
        "zaštite. Dvorski odgajivači ukrštali su tibetanske pse sa pekingezerima "
        "da bi stvorili rasu koju poznajemo, a vekovima su ih držali carevi i "
        "plemstvo. Dvadesetih i tridesetih godina XX veka nekoliko pasa "
        "stiglo je u Britaniju, gde je rasa priznata 1946. Njeno ime znači "
        "mali lav."
    ),
    "siberian-husky": (
        "Sibirski haski odgajilo je čukotsko pleme na severoistoku Sibira za "
        "vuču lakih sanki na ogromnim daljinama uz malo hrane. Psi su živeli sa "
        "porodicama i bili cenjeni zbog izdržljivosti, prijateljske naravi i "
        "gustog dvoslojnog krzna. Godine 1909. stigli su na Aljasku za trke "
        "sankama, a 1925. zaprege haskija prenele su serum protiv difterije u "
        "Nome. Rasa je priznata u SAD 1930. i danas je popularan pratilac i "
        "sportski pas."
    ),
    "sloughi": (
        "Slugi je hrt Magreba, koji su držali Berberi i Beduini u Maroku, "
        "Alžiru, Tunisu i Libiji. Lovì zečeve, gazele i divlje svinje po "
        "otvorenom prostoru i živi blizu porodice, čuvajući logor noću. Rasa "
        "se pominje u arapskoj poeziji, a u Evropu je stigla u XIX veku. "
        "Francuski klub osnovan je 1927, a međunarodno priznanje slugi je "
        "dobio 1935. godine."
    ),
    "treeing-walker-coonhound": (
        "Triing voker kunhaund razvijen je u SAD od virdžinijskih goniča koje "
        "su kolonisti doveli na zapad, pre svega od voker pasa iz Kentakija. "
        "Lovcima je bio potreban brz gonič finog njuha, koji prati trag rakuna "
        "ili medveda i zatim laje pod drvetom. Rasa je 1945. registrovana pod "
        "svojim imenom i jedan je od najpopularnijih kunhaunda u Americi. I "
        "danas je pre svega lovački pas, blage naravi u kući."
    ),
    "weimaraner": (
        "Vajmaraner potiče sa dvora u Vajmaru u Nemačkoj, gde su plemići u "
        "XIX veku odgajali svestranog lovačkog psa za krupnu divljač, ptice i "
        "rad u vodi. Nemački odgajivači držali su rasu pod strogom kontrolom: "
        "pre nego što bi štene bilo prodato, moralo je da prođe poljske "
        "ispite, a njegovi roditelji da se dokažu u radu. Prvi klub osnovan je "
        "1897, a 1929. rasa je stigla u SAD. Sivi duh baršunaste dlake postao "
        "je prepoznatljiv lovački i porodični pas."
    ),
    "whippet": (
        "Vipet potiče sa severa Engleske, gde su rudari u XIX veku odgajili "
        "malog, tihog hrta kojeg su mogli držati u maloj kući i puštati da "
        "trči po pravoj stazi posle smene. Nastao je od greyhounda i terijera i "
        "korišćen je za poteru zečeva, što se zvalo snap-dog. Trkački klubovi "
        "pojavili su se devedesetih godina XIX veka, a rasa je priznata u "
        "Britaniji 1891. Najbrži je pas svoje veličine i jedan od najmirnijih "
        "u kući."
    ),
    "wire-fox-terrier": (
        "Oštrodlaki foksterijer je britanski terijer iz oblasti lova na lisice u "
        "Engleskoj, gde mu je zadatak bio da lisicu istera iz jame kako bi "
        "goniči mogli da nastave poteru. Glatka i oštrodlaka varijanta "
        "razdvojene su klubovima osnovanim 1876, a oštrodlaka je postala "
        "popularnija. Priznata je u Britaniji 1877. i ubrzo je postala vodeći "
        "izložbeni pas, sa više titula Best in Show na Cruftsu nego bilo koja "
        "druga rasa."
    ),
    "xoloitzcuintli": (
        "Šolojskuintli, meksički bezdlaki pas, jedna je od najstarijih rasa "
        "Amerike: bezdlaki psi držani su u Meksiku više od tri hiljade godina. "
        "Asteci su ih nazvali po bogu Šolotlu i verovali da prate duše, a "
        "koristili su ih i kao iscelitelje i pratioce. U XX veku rasa je skoro "
        "nestala, a spasli su je meksički odgajivači od pedesetih godina. "
        "Meksiko ju je priznao 1956, a danas se odgaja u tri veličine, "
        "bezdlaka i obrasla."
    ),
    "yakutian-laika": (
        "Jakutska lajka drevna je autohtona rasa Republike Sahe u Sibiru, gde "
        "je radila na jednom od najhladnijih naseljenih mesta na zemlji. Psi su "
        "vukli sanke, lovili vodenu pticu i pre svega čuvali irvase, živeći uz "
        "porodice u ekstremnoj hladnoći. U sovjetskom periodu rasa je skoro "
        "izgubljena, a ruski odgajivači počeli su da je obnavljaju "
        "devedesetih godina. U Rusiji je priznata 2005, a međunarodno 2019; van "
        "Sibira je još retka."
    ),
    "yorkshire-terrier": (
        "Jorkširski terijer nastao je na severu Engleske u XIX veku, kada su se "
        "škotski tkači preselili u Jorkšir sa svojim malim terijerima. Radnici "
        "su ih ukrštali sa lokalnim terijerima da bi dobili sićušnog lovca na "
        "pacove za fabrike i rudnike, a do 1870. rasa je izlagana kao "
        "oštrodlaki škotski terijer. Priznata je u Britaniji 1886. i ubrzo je "
        "postala moderan pratilac. Danas je jedna od najmanjih rasa na svetu i "
        "popularan pas za krilo."
    ),
    "brussels-griffon": (
        "Briselski grifon potiče iz Belgije, gde su kočijaši u XIX veku držali "
        "male oštrodlake pse u stajama da love pacove i upozoravaju na "
        "nepoznate ljude. Rasa je stvorena od grifona iz staja, belgijskog "
        "uličnog psa i malog mopsa, koji joj je dao kratku njušku i gotovo "
        "ljudski izraz. Razvila su se dva tipa dlake, a glatki se danas zove "
        "peti brabanson. Belgija je priznala rasu 1904, a film Bolje ne može "
        "učinio ju je poznatom u svetu."
    ),
    # <<< END SR >>>
}
