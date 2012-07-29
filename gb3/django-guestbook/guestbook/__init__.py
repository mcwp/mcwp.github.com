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
    'Alabama': dict(twolet='AL', flower='Camellia', url='http://en.wikipedia.org/wiki/Camellia_japonica', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Camellia_japonica_flower_2.jpg/125px-Camellia_japonica_flower_2.jpg'),
    'Alaska': dict(twolet='AK', flower='Forget-me-not', url='http://en.wikipedia.org/wiki/Myosotis_alpestris', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Forget-me-not_close_600.jpg/125px-Forget-me-not_close_600.jpg'),
    'Arizona': dict(twolet='AZ', flower='Saguaro Cactus blossom', url='http://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Saguaro_cactus_blossoms.jpg/125px-Saguaro_cactus_blossoms.jpg', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Saguaro_cactus_blossoms.jpg/125px-Saguaro_cactus_blossoms.jpg'),
    'Arkansas': dict(twolet='AR', flower='Apple blossom', url='http://en.wikipedia.org/wiki/Malus', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Appletree_bloom_l.jpg/125px-Appletree_bloom_l.jpg'),
    'California': dict(twolet='CA', flower='California Poppy', url='http://en.wikipedia.org/wiki/California_Poppy', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/California_poppy.jpg/125px-California_poppy.jpg'),
    'Colorado': dict(twolet='CO', flower='Rocky Mountain Columbine', url='http://en.wikipedia.org/wiki/Aquilegia_caerulea', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Columbine_flower.JPG/125px-Columbine_flower.JPG'),
    'Connecticut': dict(twolet='CN', flower='Mountain laurel', url='http://en.wikipedia.org/wiki/Kalmia_latifolia', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Kalmia_latifolia2.jpg/125px-Kalmia_latifolia2.jpg'),
    'Deleware': dict(twolet='DE', flower='Peach blossom', url='http://en.wikipedia.org/wiki/Peach', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Peach_flowers.jpg/125px-Peach_flowers.jpg'),
    'Florida': dict(twolet='FL', flower='Orange blossom', url='http://en.wikipedia.org/wiki/Orange_(fruit)', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/OrangeBloss_wb.jpg/125px-OrangeBloss_wb.jpg'),
    'Georgia': dict(twolet='GA', flower='Cherokee Rose', url='http://en.wikipedia.org/wiki/Rosa_laevigata', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Cherokee_rose.jpg/125px-Cherokee_rose.jpg'),
    'Hawaii': dict(twolet='HI', flower='Hawaiian hibiscus', url='http://en.wikipedia.org/wiki/Hawaiian_hibiscus', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Maohauhele.jpg/125px-Maohauhele.jpg'),
    'Idaho': dict(twolet='ID', flower='Syringa Mock Orange', url='http://en.wikipedia.org/wiki/Philadelphus_lewisii', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Lewis%27s_Mock-orange_NFUW_-_Umatilla_NF_Oregon.jpg/125px-Lewis%27s_Mock-orange_NFUW_-_Umatilla_NF_Oregon.jpg'),
    'Illinois': dict(twolet='IL', flower='Violet', url='http://en.wikipedia.org/wiki/Violet_(plant)', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Viola_sororia.jpg/125px-Viola_sororia.jpg'),
    'Indiana': dict(twolet='IN', flower='Peony', url='http://en.wikipedia.org/wiki/Peony', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Paeonia_19.jpg/125px-Paeonia_19.jpg'),
    'Iowa': dict(twolet='IA', flower='Wild Prairie Rose', url='http://en.wikipedia.org/wiki/Rosa_arkansana', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Rosa_arkansana.jpg/125px-Rosa_arkansana.jpg'),
    'Kansas': dict(twolet='KS', flower='Sunflower', url='http://en.wikipedia.org/wiki/Helianthus_annuus', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/A_sunflower.jpg/125px-A_sunflower.jpg'),
    'Kentucky': dict(twolet='KY', flower='Goldenrod', url='http://en.wikipedia.org/wiki/Solidago_gigantea', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Solidago_virgaurea_minuta0.jpg/125px-Solidago_virgaurea_minuta0.jpg'),
    'Louisiana': dict(twolet='LA', flower='Magnolia', url='http://en.wikipedia.org/wiki/Magnolia', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Magnolia_wieseneri.jpg/220px-Magnolia_wieseneri.jpg'),
    'Maine': dict(twolet='ME', flower='White pine cone and tassel', url='http://en.wikipedia.org/wiki/Eastern_White_Pine', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Pinus_strobus_cones.JPG/125px-Pinus_strobus_cones.JPG'),
    'Maryland': dict(twolet='MD', flower='Black-eyed susan', url='http://en.wikipedia.org/wiki/Rudbeckia_hirta', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rudbeckia_hirta_Indian_Summer.JPG/125px-Rudbeckia_hirta_Indian_Summer.JPG'),
    'Massachusetts': dict(twolet='MA', flower='Mayflower', url='http://en.wikipedia.org/wiki/Epigaea_repens', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Trailing_arbutus.jpg/125px-Trailing_arbutus.jpg'),
    'Michigan': dict(twolet='MI', flower='Apple blossom', url='http://en.wikipedia.org/wiki/Malus', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Appletree_bloom_l.jpg/125px-Appletree_bloom_l.jpg'),
    'Minnesota': dict(twolet='MN', flower='Pink and white lady\'s slipper', url='http://en.wikipedia.org/wiki/Cypripedium_reginae', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Cypripedium_reginae_Orchi_004.jpg/125px-Cypripedium_reginae_Orchi_004.jpg'),
    'Mississippi': dict(twolet='MS', flower='Magnolia', url='http://en.wikipedia.org/wiki/Magnolia', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Magnolia_wieseneri.jpg/220px-Magnolia_wieseneri.jpg'),
    'Missouri': dict(twolet='MO', flower='Hawthorn', url='http://en.wikipedia.org/wiki/Crataegus', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Common_hawthorn_flowers.jpg/125px-Common_hawthorn_flowers.jpg'),
    'Montana': dict(twolet='MT', flower='Bitterroot', url='http://en.wikipedia.org/wiki/Bitterroot', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Lewisia_rediviva_4.jpg/125px-Lewisia_rediviva_4.jpg'),
    'Nebraska': dict(twolet='NE', flower='Goldenrod', url='http://en.wikipedia.org/wiki/Solidago_gigantea', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Solidago_virgaurea_minuta0.jpg/125px-Solidago_virgaurea_minuta0.jpg'),
    'Nevada': dict(twolet='NV', flower='Sagebrush', url='http://en.wikipedia.org/wiki/Artemisia_tridentata', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Sagebrush.jpg/125px-Sagebrush.jpg'),
    'New Hampshire': dict(twolet='NH', flower='Purple lilac', url='http://en.wikipedia.org/wiki/Syringa_vulgaris', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Lilac_%282%29.jpg/125px-Lilac_%282%29.jpg'),
    'New Jersey': dict(twolet='NJ', flower='Violet', url='http://en.wikipedia.org/wiki/Viola_sororia', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Viola_sororia.jpg/125px-Viola_sororia.jpg'),
    'New Mexico': dict(twolet='NM', flower='Yucca flower', url='http://en.wikipedia.org/wiki/Yucca', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Yukka_filamentosa.jpg/125px-Yukka_filamentosa.jpg'),
    'New York': dict(twolet='NY', flower='Rose', url='http://en.wikipedia.org/wiki/Rose', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Rosa_sp.163.jpg/125px-Rosa_sp.163.jpg'),
    'North Carolina': dict(twolet='NC', flower='Flowering Dogwood', url='http://en.wikipedia.org/wiki/Cornus_florida', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Flowering_Dogwood_Cornus_florida_Yellow_Flowers_3008px.JPG/125px-Flowering_Dogwood_Cornus_florida_Yellow_Flowers_3008px.JPG'),
    'North Dakota': dict(twolet='ND', flower='Wild Prairie Rose', url='http://en.wikipedia.org/wiki/Wild_Prairie_Rose', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Rosa_arkansana.jpg/125px-Rosa_arkansana.jpg'),
    'Ohio': dict(twolet='OH', flower='Scarlet Carnation', url='http://en.wikipedia.org/wiki/Dianthus_caryophyllus', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Red_Carnation_NGM_XXXI_p507.jpg/125px-Red_Carnation_NGM_XXXI_p507.jpg'),
    'Oklahoma': dict(twolet='OK', flower='Oklahoma Rose', url='http://en.wikipedia.org/wiki/Rosa_%27Oklahoma%27', flower_pic='http://www.okhistory.org/images/kids/rose.jpg'),
    'Oregon': dict(twolet='OR', flower='Oregon grape', url='http://en.wikipedia.org/wiki/Oregon_grape', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Mahonia_aquifolium3.jpg/125px-Mahonia_aquifolium3.jpg'),
    'Pennsylvania': dict(twolet='PA', flower='Mountain Laurel', url='http://en.wikipedia.org/wiki/Kalmia_latifolia', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Kalmia_latifolia2.jpg/125px-Kalmia_latifolia2.jpg'),
    'Rhode Island': dict(twolet='RI', flower='Violet', url='http://en.wikipedia.org/wiki/Violet_(plant)', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Viola_sororia.jpg/125px-Viola_sororia.jpg'),
    'South Carolina': dict(twolet='SC', flower='Yellow Jessamine', url='http://en.wikipedia.org/wiki/Gelsemium_sempervirens', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Gelsemium_sempervirensCDP140CA.jpg/125px-Gelsemium_sempervirensCDP140CA.jpg'),
    'South Dakota': dict(twolet='SD', flower='Pasque flower', url='http://en.wikipedia.org/wiki/Pasque_flower', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pulsatilla_vulgaris-700px.jpg/125px-Pulsatilla_vulgaris-700px.jpg'),
    'Tennassee': dict(twolet='TN', flower='Iris', url='http://en.wikipedia.org/wiki/Iris_(plant)', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Iris_%27Gene_Wild%27_2007-05-13_383.jpg/125px-Iris_%27Gene_Wild%27_2007-05-13_383.jpg'),
    'Texas': dict(twolet='TX', flower='Bluebonnet', url='http://en.wikipedia.org/wiki/Lupinus_texensis', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Texas_Bluebonnet_%28Lupinus_texensis%29.jpg/125px-Texas_Bluebonnet_%28Lupinus_texensis%29.jpg'),
    'Utah': dict(twolet='UT', flower='Sego lily', url='http://en.wikipedia.org/wiki/Calochortus_nuttallii', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Sego_lily_cm.jpg/125px-Sego_lily_cm.jpg'),
    'Vermont': dict(twolet='VT', flower='Red Clover', url='http://en.wikipedia.org/wiki/Trifolium_pratense', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Red_clover_closeup.jpg/125px-Red_clover_closeup.jpg'),
    'Verginia': dict(twolet='VA', flower='American Dogwood', url='http://en.wikipedia.org/wiki/Cornus_florida', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Benthamidia_florida2.jpg/125px-Benthamidia_florida2.jpg'),
    'Washington': dict(twolet='WA', flower='Coast Rhododendron', url='http://en.wikipedia.org/wiki/Rhododendron_macrophyllum', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Rhododendron_macrophyllum.JPG/125px-Rhododendron_macrophyllum.JPG'),
    'West Verginia': dict(twolet='WV', flower='Rhododendron', url='http://en.wikipedia.org/wiki/Rhododendron', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Rhododendron-by-eiffel-public-domain-20040617.jpg/125px-Rhododendron-by-eiffel-public-domain-20040617.jpg'),
    'Wisconsin': dict(twolet='WI', flower='Wood Violet', url='http://en.wikipedia.org/wiki/Viola_sororia', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Viola_sororia.jpg/125px-Viola_sororia.jpg'),
    'Wyoming': dict(twolet='WY', flower='Indian Paintbrush', url='http://en.wikipedia.org/wiki/Castilleja_linariifolia', flower_pic='http://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Indian_Paintbrush_in_Grand_Teton_NP-NPS.jpg/125px-Indian_Paintbrush_in_Grand_Teton_NP-NPS.jpg')
    }

pic_urls = {}
for state in stateflowers.keys():
    pic_urls[state] = stateflowers[state]['flower_pic']

five_states =  stateflowers.keys()[:5]

shorter = {}

for state in five_states:
    shorter[state] = stateflowers[state]['flower_pic']
    


#logging.info('State names %s', type(state_names))

for n in state_names:
    logging.info('try state %s', n)
#    x = State(n)
    x = State.objects.create(name=n)
#    x.save()

logging.info('x is %s', str(x))
logging.info(dir(x))
logging.info('x name is %s', str(x.name))
