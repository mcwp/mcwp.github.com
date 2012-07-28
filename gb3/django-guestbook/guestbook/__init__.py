from guestbook.models import State
import logging

state_names = [
    'California',
    'Oregon',
    'Nevada',
    'Utah',
    'Arizona',
    ]


stateflowers = {
    'Alabama': dict(twolet='AL', flower='Camellia', url='http://en.wikipedia.org/wiki/Camellia_japonica', flower_pic=''),
    'Alaska': dict(twolet='AK', flower='Forget-me-not', url='http://en.wikipedia.org/wiki/Myosotis_alpestris', flower_pic=''),
    'Arizona': dict(twolet='AZ', flower='Saguaro Cactus blossom', url='http://en.wikipedia.org/wiki/Saguaro', flower_pic=''),
    'Arkansas': dict(twolet='AR', flower='Apple blossom', url='http://en.wikipedia.org/wiki/Malus', flower_pic=''),
    'California': dict(twolet='CA', flower='California Poppy', url='http://en.wikipedia.org/wiki/California_Poppy', flower_pic=''),
    'Colorado': dict(twolet='CO', flower='Rocky Mountain Columbine', url='http://en.wikipedia.org/wiki/Aquilegia_caerulea', flower_pic=''),
    'Connecticut': dict(twolet='CN', flower='Mountain laurel', url='http://en.wikipedia.org/wiki/Kalmia_latifolia', flower_pic=''),
    'Deleware': dict(twolet='DE', flower='Peach blossom', url='http://en.wikipedia.org/wiki/Peach', flower_pic=''),
    'Florida': dict(twolet='FL', flower='Orange blossom', url='http://en.wikipedia.org/wiki/Orange_(fruit)', flower_pic=''),
    'Georgia': dict(twolet='GA', flower='Cherokee Rose', url='http://en.wikipedia.org/wiki/Rosa_laevigata', flower_pic=''),
    'Hawaii': dict(twolet='HI', flower='Hawaiian hibiscus', url='http://en.wikipedia.org/wiki/Hawaiian_hibiscus', flower_pic=''),
    'Idaho': dict(twolet='ID', flower='Syringa Mock Orange', url='http://en.wikipedia.org/wiki/Philadelphus_lewisii', flower_pic=''),
    'Illinois': dict(twolet='IL', flower='Violet', url='http://en.wikipedia.org/wiki/Violet_(plant)', flower_pic=''),
    'Indiana': dict(twolet='IN', flower='Peony', url='http://en.wikipedia.org/wiki/Peony', flower_pic=''),
    'Iowa': dict(twolet='IA', flower='Wild Prairie Rose', url='http://en.wikipedia.org/wiki/Rosa_arkansana', flower_pic=''),
    'Kansas': dict(twolet='KS', flower='Sunflower', url='http://en.wikipedia.org/wiki/Helianthus_annuus', flower_pic=''),
    'Kentucky': dict(twolet='KY', flower='Goldenrod', url='http://en.wikipedia.org/wiki/Solidago_gigantea', flower_pic=''),
    'Louisiana': dict(twolet='LA', flower='Magnolia', url='http://en.wikipedia.org/wiki/Magnolia', flower_pic=''),
    'Maine': dict(twolet='ME', flower='White pine cone and tassel', url='http://en.wikipedia.org/wiki/Eastern_White_Pine', flower_pic=''),
    'Maryland': dict(twolet='MD', flower='Black-eyed susan', url='http://en.wikipedia.org/wiki/Rudbeckia_hirta', flower_pic=''),
    'Massachusetts': dict(twolet='MA', flower='Mayflower', url='http://en.wikipedia.org/wiki/Epigaea_repens', flower_pic=''),
    'Michigan': dict(twolet='MI', flower='Apple blossom', url='http://en.wikipedia.org/wiki/Malus', flower_pic=''),
    'Minnesota': dict(twolet='MN', flower='Pink and white lady\'s slipper', url='http://en.wikipedia.org/wiki/Cypripedium_reginae', flower_pic=''),
    'Mississippi': dict(twolet='MS', flower='Magnolia', url='http://en.wikipedia.org/wiki/Magnolia', flower_pic=''),
    'Missouri': dict(twolet='MO', flower='Hawthorn', url='http://en.wikipedia.org/wiki/Crataegus', flower_pic=''),
    'Montana': dict(twolet='MT', flower='Bitterroot', url='http://en.wikipedia.org/wiki/Bitterroot', flower_pic=''),
    'Nebraska': dict(twolet='NE', flower='Goldenrod', url='http://en.wikipedia.org/wiki/Solidago_gigantea', flower_pic=''),
    'Nevada': dict(twolet='NV', flower='Sagebrush', url='http://en.wikipedia.org/wiki/Artemisia_tridentata', flower_pic=''),
    'New Hampshire': dict(twolet='NH', flower='Purple lilac', url='http://en.wikipedia.org/wiki/Syringa_vulgaris', flower_pic=''),
    'New Jersey': dict(twolet='NJ', flower='Violet', url='http://en.wikipedia.org/wiki/Viola_sororia', flower_pic=''),
    'New Mexico': dict(twolet='NM', flower='Yucca flower', url='http://en.wikipedia.org/wiki/Yucca', flower_pic=''),
    'New York': dict(twolet='NY', flower='Rose', url='http://en.wikipedia.org/wiki/Rose', flower_pic=''),
    'North Carolina': dict(twolet='NC', flower='Flowering Dogwood', url='http://en.wikipedia.org/wiki/Cornus_florida', flower_pic=''),
    'North Dakota': dict(twolet='ND', flower='Wild Prairie Rose', url='http://en.wikipedia.org/wiki/Wild_Prairie_Rose', flower_pic=''),
    'Ohio': dict(twolet='OH', flower='Scarlet Carnation', url='http://en.wikipedia.org/wiki/Dianthus_caryophyllus', flower_pic=''),
    'Oklahoma': dict(twolet='OK', flower='Oklahoma Rose', url='http://en.wikipedia.org/wiki/Rosa_%27Oklahoma%27', flower_pic=''),
    'Oregon': dict(twolet='OR', flower='Oregon grape', url='http://en.wikipedia.org/wiki/Oregon_grape', flower_pic=''),
    'Pennsylvania': dict(twolet='PA', flower='Mountain Laurel', url='http://en.wikipedia.org/wiki/Kalmia_latifolia', flower_pic=''),
    'Rhode Island': dict(twolet='RI', flower='Violet', url='http://en.wikipedia.org/wiki/Violet_(plant)', flower_pic=''),
    'South Carolina': dict(twolet='SC', flower='Yellow Jessamine', url='http://en.wikipedia.org/wiki/Gelsemium_sempervirens', flower_pic=''),
    'South Dakota': dict(twolet='SD', flower='Pasque flower', url='http://en.wikipedia.org/wiki/Pasque_flower', flower_pic=''),
    'Tennassee': dict(twolet='TN', flower='Iris', url='http://en.wikipedia.org/wiki/Iris_(plant)', flower_pic=''),
    'Texas': dict(twolet='TX', flower='Bluebonnet', url='http://en.wikipedia.org/wiki/Lupinus_texensis', flower_pic=''),
    'Utah': dict(twolet='UT', flower='Sego lily', url='http://en.wikipedia.org/wiki/Calochortus_nuttallii', flower_pic=''),
    'Vermont': dict(twolet='VT', flower='Red Clover', url='http://en.wikipedia.org/wiki/Trifolium_pratense', flower_pic=''),
    'Verginia': dict(twolet='VA', flower='American Dogwood', url='http://en.wikipedia.org/wiki/Cornus_florida', flower_pic=''),
    'Washington': dict(twolet='WA', flower='Coast Rhododendron', url='http://en.wikipedia.org/wiki/Rhododendron_macrophyllum', flower_pic=''),
    'West Verginia': dict(twolet='WV', flower='Rhododendron', url='http://en.wikipedia.org/wiki/Rhododendron', flower_pic=''),
    'Wisconsin': dict(twolet='WI', flower='Wood Violet', url='http://en.wikipedia.org/wiki/Viola_sororia', flower_pic=''),
    'Wyoming': dict(twolet='WY', flower='Indian Paintbrush', url='http://en.wikipedia.org/wiki/Castilleja_linariifolia', flower_pic='')
    }
    


#logging.info('State names %s', type(state_names))

for n in state_names:
    logging.info('try state %s', n)
#    x = State(n)
    x = State.objects.create(name=n)
#    x.save()

logging.info('x is %s', str(x))
logging.info(dir(x))
logging.info('x name is %s', str(x.name))
