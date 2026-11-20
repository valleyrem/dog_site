from django.db import migrations

EN = {
    "summary": "Bold, loud and devoted to its people. The Dachshund is a small dog with the mind of a hunter: curious, independent and very sure of itself.",
    "good_fit": "Want a companion that follows you from room to room\nAre patient and keep training short, calm and rewarding\nLive in a flat and can carry the dog on stairs or have a lift\nCan accept a dog that listens when it suits it",
    "think_twice": "Are away from home most of the day\nShare a home with hamsters, rabbits or other small pets\nHave very noise-sensitive neighbours\nWant a dog for long jogs or climbing and jumping games",
    "daily_life": "Two or three walks add up to about an hour a day, with a sniff-heavy route rather than a sprint. It is happy in a flat as long as it gets that time and your company.\nAlone for a few hours is fine once it is used to it, but a bored Dachshund digs, chews and barks. Expect a surprisingly big voice for a small dog, so neighbours are worth a thought.\nWith children it is loyal and playful, provided kids handle it gently and never lift it by the front legs. Other dogs are usually fine; small pets are seen as prey.\nCoat care depends on the variety: smooth coats need a weekly wipe, long coats a brush a few times a week, wire coats a brush and occasional trimming.",
    "quirks": "Dachshunds love tunnels: expect your dog under the blankets, inside cushions and in the garden flower bed.\nThe nose leads. On a walk it may stop for a minute at one spot and refuse to move on.\nThey choose a favourite person and can be a little jealous of everyone else.",
    "history": "The Dachshund was developed in Germany from short-legged hunting dogs that could follow badgers and foxes into their dens. The name means badger dog, and the breed appears in German records from the fifteenth century. Three coat types and two sizes were bred for different quarry, and in Britain the breed was recognised in 1881.",
    "care": "Keep your Dachshund lean: extra weight is hard on a long back. Use ramps or steps for the sofa and car, do not let it jump from heights, and support its chest and hindquarters when you lift it. Brush according to coat type, check ears and teeth regularly, and book routine vet visits. Ask the breeder about the parents' health checks.",
}
RU = {
    "summary": "Смелая, громкая и очень преданная своим людям. Такса — маленькая собака с умом охотника: любопытная, самостоятельная и уверенная в себе.",
    "good_fit": "Хотите компаньона, который ходит за вами из комнаты в комнату\nТерпеливы и проводите занятия коротко, спокойно и с поощрением\nЖивёте в квартире и готовы носить собаку по лестнице или у вас есть лифт\nПримете собаку, которая слушается, когда ей удобно",
    "think_twice": "Большую часть дня не бываете дома\nЖивёте с хомяками, кроликами и другими мелкими животными\nУ вас очень чувствительные к шуму соседи\nХотите собаку для долгих пробежек и игр с прыжками",
    "daily_life": "Две–три прогулки в сумме около часа в день: лучше спокойный маршрут с нюханием, чем бег. В квартире ей хорошо, если есть это время и ваша компания.\nНесколько часов в одиночестве — нормально, когда она привыкла, но заскучавшая такса роет, грызёт и лает. Голос у неё неожиданно громкий для маленькой собаки, так что стоит подумать о соседях.\nС детьми она преданная и игривая, если дети обращаются бережно и не поднимают её за передние лапы. С другими собаками обычно ладит, мелких животных воспринимает как добычу.\nУход зависит от разновидности: гладкошёрстную достаточно протирать раз в неделю, длинношёрстную расчёсывать несколько раз в неделю, жёсткошёрстную расчёсывать и иногда тримминговать.",
    "quirks": "Таксы любят норы: ваша собака будет под одеялом, в подушках и в клумбе.\nВедёт нос. На прогулке она может минуту стоять на одном месте и не хотеть идти дальше.\nОни выбирают любимого человека и могут немного ревновать к остальным.",
    "history": "Такса выведена в Германии из короткоголовых охотничьих собак, способных идти за барсуком и лисой в нору. Название означает «барсучья собака», а в немецких записях порода встречается с XV века. Три типа шерсти и два размера создавали под разную добычу, а в Британии порода признана в 1881 году.",
    "care": "Следите, чтобы такса не полнела: лишний вес тяжело сказывается на длинной спине. Используйте пандус или ступеньки для дивана и машины, не давайте прыгать с высоты и поддерживайте грудь и заднюю часть, когда берёте на руки. Расчёсывайте по типу шерсти, регулярно проверяйте уши и зубы и ходите на плановые осмотры к ветеринару. Спросите заводчика о проверках здоровья родителей.",
}
PARAMS = dict(
    exercise_minutes="45–75",
    alone_tolerance="medium",
    good_with_pets="careful",
    first_time_owner="patient",
    prey_drive="high",
)


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    values = dict(PARAMS)
    for key, text in EN.items():
        values[key] = text
        values[key + "_en"] = text
    for key, text in RU.items():
        values[key + "_ru"] = text
    Dogs.objects.filter(slug="dachshund").update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0050_breed_page_layout")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
