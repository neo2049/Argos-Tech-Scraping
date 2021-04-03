# -*- coding: utf-8 -*-
import products
import jump_menus

tech = jump_menus.\
    menu_links('https://www.argos.co.uk/browse/technology/c:29949/?clickOrigin=header:home:menu:technology')

# Technology Products
mobile_phones_accessories = jump_menus.menu_links(tech['Mobile phones and accessories'])
laptops_pcs = jump_menus.menu_links(tech['Laptops and PCs'])
tvs_accessories = jump_menus.menu_links(tech['Televisions and accessories'])
tablets = jump_menus.menu_links(tech['Tablets and iPad'])
ereaders = jump_menus.menu_links(tech['Kindle and e-readers'])
tablet_accessories = jump_menus.menu_links(tech['Tablet, iPad and E-reader accessories'])
videogames = jump_menus.menu_links(tech['Video games and consoles'])
cameras = jump_menus.menu_links(tech['Cameras'])
camcorders = jump_menus.menu_links(tech['Camcorders'])
home_audio = jump_menus.menu_links(tech['Home audio'])
portable_audio = jump_menus.menu_links(tech['iPod, MP3 and headphones'])
telephones_accessories = jump_menus.menu_links(tech['Telephones and accessories'])
home_cinema = jump_menus.menu_links(tech['DVD players, blu-ray players and home cinema'])
set_top_boxes = jump_menus.menu_links(tech['Set top boxes, recorders and satellite'])
smart_tech = jump_menus.menu_links(tech['Smart technology'])
dash_cams = jump_menus.menu_links(tech['Dash cams'])
batteries = jump_menus.menu_links(tech['Household batteries and battery chargers'])
sat_nav = jump_menus.menu_links(tech['Sat navs and accessories'])
car_radio = jump_menus.menu_links(tech['In-car radios, CD and DVD players'])
dvd = jump_menus.menu_links(tech['DVDs and blu-ray'])

# Mobile phone products
products.product_page(products.pagination(mobile_phones_accessories['SIM free phones']), 'sim_free_phones')
products.product_page(products.pagination(mobile_phones_accessories['Pay as you go phones']), 'payg')
products.product_page(products.pagination(mobile_phones_accessories['Smart watches']), 'smart_watches')
products.product_page(products.pagination(mobile_phones_accessories['Mobile phone cases']), 'mobile_phone_cases')
products.product_page(products.pagination(mobile_phones_accessories['Mobile USB Storage']), 'mobile_usb_storage')
products.product_page(products.pagination(mobile_phones_accessories['MicroSD memory cards']), 'micro_sd_card')
products.product_page(products.pagination(mobile_phones_accessories['Mobile phone accessories']), 'mobile_accessories')
products.product_page(products.pagination(mobile_phones_accessories['Mobile phone chargers and adaptors']),
                      'mobile_chargers')
products.product_page(products.pagination(mobile_phones_accessories['Mobile phone headsets, '
                                                                    'headphones and microphones']),
                      'mobile_headsets')
products.product_page(products.pagination(mobile_phones_accessories['Mobile phone screen protectors']),
                      'mobile_screen_protectors')
products.product_page(products.pagination(mobile_phones_accessories['Portable power banks']), 'power_banks')
products.product_page(products.pagination(mobile_phones_accessories['Mobile phone SIM cards']), 'sim_cards')

# Telephones
products.product_page(products.pagination(mobile_phones_accessories['Telephones']), 'telephoones')

# PCs and Laptops
products.product_page(products.pagination(laptops_pcs['Laptops and netbooks']), 'laptops')
computer_accessories = jump_menus.menu_links(laptops_pcs['Laptop and PC accessories'])
products.product_page(products.pagination(computer_accessories['Laptop and PC mice']), 'mice')
products.product_page(products.pagination(computer_accessories['PC keyboards']), 'keyboards')
products.product_page(products.pagination(computer_accessories['Computer Cables']), 'computer_cables')
products.product_page(products.pagination(computer_accessories['CD and DVD rewriters']), 'cd_rewriters')
products.product_page(products.pagination(computer_accessories['USB hubs']), 'usb_hubs')
products.product_page(products.pagination(computer_accessories['Webcams']), 'webcams')
products.product_page(products.pagination(computer_accessories['Graphic tablets and accessories']), 'graphic_tablet')
products.product_page(products.pagination(computer_accessories['Mouse mats']), 'mouse_mat')
products.product_page(products.pagination(computer_accessories['Blank CDs and DVDs']), 'blank_cd')
products.product_page(products.pagination(computer_accessories['Gaming capture cards and streaming']),
                      'gaming_capture_cards')
products.product_page(products.pagination(computer_accessories['Laptop bags, cases and skins']), 'laptop_bags')
products.product_page(products.pagination(computer_accessories['Laptop trays and stands']), 'laptop_stands')
products.product_page(products.pagination(computer_accessories['Laptop and MacBook chargers']), 'laptop_chargers')
products.product_page(products.pagination(computer_accessories['Laptop Security Cables']), 'laptop_security_cables')
products.product_page(products.pagination(computer_accessories['Laptop and PC speakers']), 'pc_speakers')
products.product_page(products.pagination(computer_accessories['USB microphones']), 'usb_microphones')
products.product_page(products.pagination(computer_accessories['Laptop and PC headsets']), 'computer_headsets')
products.product_page(products.pagination(laptops_pcs['Desktop computers and all in ones']), 'desktops')
products.product_page(products.pagination(laptops_pcs['Gaming laptops and PCs']), 'gaming_computers')
products.product_page(products.pagination(laptops_pcs['Macbook']), 'macbook')
products.product_page(products.pagination(laptops_pcs['Chromebooks']), 'chromebooks')
products.product_page(products.pagination(laptops_pcs['Laptop and PC software']), 'software')
components = products.pagination(laptops_pcs['Desktop computer components'])
products.product_page(products.pagination(components['All Desktop computer components']), 'desktop_components')
monitors = products.pagination(laptops_pcs['PC monitors and stands'])
products.product_page(products.pagination(monitors['PC monitors']), 'monitors')
products.product_page(products.pagination(monitors['PC monitor stands and brackets']), 'monitor_stands')
products.product_page(products.pagination(laptops_pcs['iMacs']), 'imacs')
products.product_page(products.pagination(laptops_pcs['Mobile broadband']), 'mobile_broadband')
external_storage = products.pagination(laptops_pcs['External hard drives and USB storage'])
products.product_page(products.pagination(external_storage['External hard drives']), 'external_hdd')
products.product_page(products.pagination(external_storage['USB storage']), 'usb_storage')
networking = products.pagination(laptops_pcs['Networking'])
products.product_page(products.pagination(networking['Powerlines']), 'powerlines')
products.product_page(products.pagination(networking['Wi-Fi boosters']), 'wifi_boosters')
products.product_page(products.pagination(networking['Wi-Fi routers']), 'wifi_routers')
products.product_page(products.pagination(networking['USB Wi-Fi adapters']), 'usb_wifi_adapters')
products.product_page(products.pagination(networking['Network switches']), 'network_switches')

# TVs and accessories
products.product_page(products.pagination(tvs_accessories['Televisions']), 'tv')
aerials = products.pagination(tvs_accessories['TV aerials, boosters and accessories'])
products.product_page(products.pagination(aerials['TV aerials']), 'tv_aerials')
products.product_page(products.pagination(aerials['TV signal boosters']), 'tv_signal_boosters')
products.product_page(products.pagination(aerials['TV aerials cables and accessories']), 'tv_aerials_accessories')
tv_stands = products.pagination(tvs_accessories['TV stands and wall brackets'])
products.product_page(products.pagination(tv_stands['TV wall brackets']), 'tv_wall_brackets')
products.product_page(products.pagination(tv_stands['TV stands']), 'tv_stands')
products.product_page(products.pagination(tv_stands['TV wall bracket accessories']), 'tv_wall_bracket_accessories')
products.product_page(products.pagination(tv_stands['TV frames']), 'tv_frames')
products.product_page(products.pagination(tvs_accessories['HDMI cables and optical cables']), 'tv_cables')
products.product_page(products.pagination(tvs_accessories['TV remote controls']), 'tv_remote')

# Tablets
products.product_page(products.pagination(tablets['Tablets']), 'tablets')
products.product_page(products.pagination(tablets['iPad']), 'ipad')
products.product_page(products.pagination(tablets['iPad and tablet covers and cases']), 'tablet_covers')
products.product_page(products.pagination(tablets['Kindle and e-readers']), 'kindle')
products.product_page(products.pagination(tablets['Kindle and e-reader cases and covers']), 'kindle_covers')
products.product_page(products.pagination(tablets['iPad and tablet chargers']), 'tablet_chargers')
products.product_page(products.pagination(tablets['iPad and tablet adapters']), 'tablet_adapters')
products.product_page(products.pagination(tablets['iPad and tablet accessories']), 'tablet_accessories')


# Videogames
products.product_page(products.pagination(videogames['PS4']), 'ps4')
products.product_page(products.pagination(videogames['PS3']), 'ps3')
products.product_page(products.pagination(videogames['Xbox One']), 'xbox_one')
products.product_page(products.pagination(videogames['Xbox 360']), 'xbox_360')
products.product_page(products.pagination(videogames['Nintendo Switch']), 'nintendo_switch')
products.product_page(products.pagination(videogames['Nintendo 2DS and 2DS XL']), 'nintendo_2ds')
products.product_page(products.pagination(videogames['Nintendo Wii games']), 'nintendo_wii')
products.product_page(products.pagination(videogames['PC gaming']), 'pc_gaming')
products.product_page(products.pagination(videogames['Pre-order games']), 'videogames_preorder')
products.product_page(products.pagination(videogames['Retro gaming consoles']), 'retro_gaming')
products.product_page(products.pagination(videogames['Toys to Life']), 'toys_to_life')
products.product_page(products.pagination(videogames['Gaming chairs']), 'gaming_chairs')
products.product_page(products.pagination(videogames['Gaming headsets']), 'gaming_headsets')
products.product_page(products.pagination(videogames['Virtual Reality Headsets']), 'vr')
products.product_page(products.pagination(videogames['Gaming capture cards and streaming']), 'streaming')
products.product_page(products.pagination(videogames['Gaming guides']), 'gaming_guides')


# Cameras
cameras = products.pagination(cameras['Cameras'])
products.product_page(products.pagination(cameras['Compact digital cameras']), 'compact_cameras')
products.product_page(products.pagination(cameras['Instant cameras']), 'instant_cameras')
products.product_page(products.pagination(cameras['Bridge digital cameras']), 'bridge_digital_cameras')
products.product_page(products.pagination(cameras['DSLR cameras']), 'dslr_cameras')
products.product_page(products.pagination(cameras['Superzoom cameras']), 'superzoom_cameras')
products.product_page(products.pagination(cameras['Mirrorless cameras']), 'mirrorless_cameras')
products.product_page(products.pagination(cameras['Kids cameras']), 'kids_cameras')
products.product_page(products.pagination(cameras['Waterproof cameras']), 'waterproof_cameras')
camcorders = products.pagination(cameras['Camcorders'])
products.product_page(products.pagination(camcorders['Traditional camcorders']), 'traditional_camcorders')
products.product_page(products.pagination(camcorders['Tough and action camcorders']), 'action_cameras')
products.product_page(products.pagination(camcorders['Tough and action camcorder accessories']),
                      'action_cameras_accessories')
products.product_page(products.pagination(camcorders['Camcorder cases and bags']), 'camcorder_bags_accessories')
products.product_page(products.pagination(cameras['Camera bags and cases']), 'camera_bags')
products.product_page(products.pagination(cameras['Tripods, monopods and cases']), 'tripods')
products.product_page(products.pagination(cameras['Digital photo frames']), 'digital_frames')
products.product_page(products.pagination(cameras['Memory cards and readers']), 'memory_cards')
products.product_page(products.pagination(cameras['Film and disposable cameras']), 'film_disposable_cameras')
products.product_page(products.pagination(cameras['Camera lenses and lens accessories']), 'camera_lens')
products.product_page(products.pagination(cameras['Camera filters and flashes']), 'camera_filters')
products.product_page(products.pagination(cameras['Photographic accessories and editing software']),
                      'photo_accessories_software')
products.product_page(products.pagination(cameras['Camcorder accessories']), 'camcorder_accessories')
products.product_page(products.pagination(cameras['Digital photo printers, paper and ink']), 'photo_printers')
products.product_page(products.pagination(cameras['Camera batteries']), 'camera_batteries')


# Home audio
hifi = products.pagination(home_audio['Hi-fi systems'])
bluetooth_speakers = products.pagination(home_audio['Wireless and Bluetooth speakers'])
personal_cd_cassette = products.pagination(home_audio['Personal CD players and cassette players'])
radio = products.pagination(home_audio['Radios'])
record_players = products.pagination(home_audio['Record players and turntables'])
clock_radios = products.pagination(home_audio['Clock radios'])
audio_accessories = products.pagination(home_audio['Audio accessories'])
smart_speakers = products.pagination(home_audio['Smart speakers'])
karaoke = products.pagination(home_audio['Karaoke machines and equipment'])
personal_radios = products.pagination(home_audio['Personal radios'])
cd_vinyl = products.pagination(home_audio['CDs and vinyl'])


# Portable Audio
headphones = products.pagination(portable_audio['Headphones and earphones'])
mp3_players = products.pagination(portable_audio['MP3 players'])
ipod = products.pagination(portable_audio['iPod'])
ipod_accessories = products.pagination(portable_audio['iPod accessories'])
mp3_accessories = products.pagination(portable_audio['MP3 accessories'])
ipod_cases = products.pagination(portable_audio['iPod skins, cases and holders'])

# Telephone accessories
telephones = products.pagination(telephones_accessories['Telephones'])
phone_accessories = products.pagination(telephones_accessories['Telephone accessories'])

# Home cinema
dvd_players = products.pagination(home_cinema['DVD players and recorders'])
blue_ray_players = products.pagination(home_cinema['Blu-ray players'])
home_cinema_products = products.pagination(home_cinema['Home cinema systems and sound bars'])
portable_dvd = products.pagination(home_cinema['Portable DVD players and accessories'])
hdmi_cables = products.pagination(home_cinema['HDMI, SCART cables and adapters'])

# Set top boxes
smart_tv_box = products.pagination(set_top_boxes['Smart TV boxes'])
digital_tv_recorders = products.pagination(set_top_boxes['Digital TV recorders'])
freeview = products.pagination(set_top_boxes['Freeview and freesat'])

# Smart tech
smart_home_monitoring = products.pagination(smart_tech['Smart home monitoring'])
smart_security = products.pagination(smart_tech['Smart security and CCTV'])
smart_doorbells = products.pagination(smart_tech['Smart doorbells'])
Smart_speakers = products.pagination(smart_tech['Smart speakers'])
smart_heating = products.pagination(smart_tech['Smart heating'])
smart_lighting = products.pagination(smart_tech['Smart lighting'])
smart_hubs = products.pagination(smart_tech['Smart hubs'])
smart_plugs = products.pagination(smart_tech['Smart plugs'])
smart_watches = products.pagination(smart_tech['Smart watches'])
fitness_trackers = products.pagination(smart_tech['Fitness and activity trackers'])

# Dash Cams
dash_cam_products = products.pagination(tech['Dash cams'])

# Batteries
battery = products.pagination(tech['Household batteries and battery chargers'])

# sat nav
sat_nav_products = products.pagination(sat_nav['Sat nav'])
sat_nav_mounts = products.pagination(sat_nav['Sat nav mounts'])
sat_nav_accessory_kits = products.pagination(sat_nav['Sat nav accessory kits'])
sat_nav_cases = products.pagination(sat_nav['Sat nav cases'])

# car radio
car_radio_products = products.pagination(car_radio['In car DAB and CD car radios'])
car_dvd = products.pagination(car_radio['In car DVD players'])
car_audio_accessories = products.pagination(car_radio['In car DAB and CD car radio accessories'])
in_car_chargers = products.pagination(car_radio['In-car chargers'])

# DVD and Blue-Ray Movies
movies = products.pagination(tech['DVDs and blu-ray'])
