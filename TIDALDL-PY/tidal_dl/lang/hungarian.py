#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hungarian.py
@Time    :   2022/08/01
@Author  :   Shanahan
@Version :   1.2
@Contact :   
@Desc    :   
'''


class LangHungarian(object):
    SETTING = "BEÁLLÍTÁSOK"
    VALUE = "ÉRTÉK"
    SETTING_DOWNLOAD_PATH = "Letöltési útvonal"
    SETTING_ONLY_M4A = "mp4 konvertálása m4a-ra"
    SETTING_ADD_EXPLICIT_TAG = "Explicit tag hozzáadása"
    SETTING_ADD_HYPHEN = "Kötőjel hozzáadása"
    SETTING_ADD_YEAR = "Év hozzáadása az album-mappa előtt"
    SETTING_USE_TRACK_NUM = "Add user track number"
    SETTING_AUDIO_QUALITY = "Audió minősége"
    SETTING_VIDEO_QUALITY = "Videó minősége"
    SETTING_CHECK_EXIST = "Ellenőrizze, hogy létezik-e"
    SETTING_ARTIST_BEFORE_TITLE = "Előadó neve a szám címe előtt"
    SETTING_ALBUMID_BEFORE_FOLDER = "Azonosító (ID) az album-mappa előtt"
    SETTING_INCLUDE_EP = "Tartalmazza a single&ep"
    SETTING_SAVE_COVERS = "Borítókép mentése"
    SETTING_LANGUAGE = "Nyelv"
    SETTING_USE_PLAYLIST_FOLDER = "Lejátszási lista mappa használata"
    SETTING_MULITHREAD_DOWNLOAD = "Többszálú letöltés"
    SETTING_ALBUM_FOLDER_FORMAT = "Album mappa formátum"
    SETTING_PLAYLIST_FOLDER_FORMAT = "Playlist folder format"
    SETTING_TRACK_FILE_FORMAT = "Track fájlformátum"
    SETTING_VIDEO_FILE_FORMAT = "Videó fájlformátum"
    SETTING_SHOW_PROGRESS = "Haladás megjelenítése"
    SETTING_SHOW_TRACKINFO = "Track infók megjelenítése"
    SETTING_SAVE_ALBUMINFO = "AlbumInfo.txt mentése"
    SETTING_ADD_LYRICS = "Dalszöveg hozzáadása"
    SETTING_LYRICS_SERVER_PROXY = "Dalszöveg kiszolgáló proxy"
    SETTING_ADD_LRC_FILE = "Dalszövegek mentése (.lrc fájl)"
    SETTING_PATH = "Beállítási útvonal"
    SETTING_APIKEY = "APIKey támogatás"
    SETTING_ADD_TYPE_FOLDER = "Mappa típus hozzáadása"

    CHOICE = "VÁLASZTÁS"
    FUNCTION = "FUNKCIÓ"
    CHOICE_ENTER = "Írja be a"
    CHOICE_ENTER_URLID = "Adja meg az 'Url/ID'-t:"
    CHOICE_EXIT = "Kilépés"
    CHOICE_LOGIN = "AccessToken ellenőrzése"
    CHOICE_SETTINGS = "Beállítások"
    CHOICE_SET_ACCESS_TOKEN = "AccessToken beállítása"
    CHOICE_DOWNLOAD_BY_URL = "Letöltés URL vagy ID alapján"
    CHOICE_LOGOUT = "Kijelentkezés"
    CHOICE_APIKEY = "APIKey kiválasztása"

    PRINT_ERR = "[HIBA]"
    PRINT_INFO = "[INFÓ]"
    PRINT_SUCCESS = "[SIKERES]"

    PRINT_ENTER_CHOICE = "Válasszon:"
    PRINT_LATEST_VERSION = "Legújabb verzió:"
    # PRINT_USERNAME = "felhasználónév:"
    # PRINT_PASSWORD = "jelszó:"

    CHANGE_START_SETTINGS = "Beállítások indítása('0'- Vissza, '1'-Igen):"
    CHANGE_DOWNLOAD_PATH = "Letöltési útvonal('0' nincs módosítás):"
    CHANGE_AUDIO_QUALITY = "Audió minőség('0'-Normal,'1'-High,'2'-HiFi,'3'-Master):"
    CHANGE_VIDEO_QUALITY = "Videó minőség(1080, 720, 480, 360):"
    CHANGE_ONLYM4A = "mp4 átalakítása m4a-ra('0'-Nem,'1'-Igen):"
    CHANGE_ADD_EXPLICIT_TAG = "Explicit tag hozzáadása a fájlnevekhez('0'-Nem,'1'-Igen):"
    CHANGE_ADD_HYPHEN = "Kötőjel használata szóköz helyett a fájlnevekben('0'-Nem,'1'-Igen):"
    CHANGE_ADD_YEAR = "Évszám hozzáadása az album mappanevekhez('0'-Nem,'1'-Igen):"
    CHANGE_USE_TRACK_NUM = "Track szám hozzáadása a fájlnevek előtt('0'-Nem,'1'-Igen):"
    CHANGE_CHECK_EXIST = "Létező fájl ellenőrzése letöltés előtt('0'-Nem,'1'-Igen):"
    CHANGE_ARTIST_BEFORE_TITLE = "Előadó hozzáadása a szám címe előtt('0'-Nem,'1'-Igen):"
    CHANGE_INCLUDE_EP = "A kislemezek és EP-k letöltése('0'-Nem, '1'-Igen):"
    CHANGE_ALBUMID_BEFORE_FOLDER = "Azonosító (ID) az album mappa előtt('0'-Nem,'1'-Igen):"
    CHANGE_SAVE_COVERS = "Borító mentése('0'-Nem, '1'-Igen):"
    CHANGE_LANGUAGE = "Nyelv kiválasztása"
    CHANGE_ALBUM_FOLDER_FORMAT = "Album mappa formátum('0' nincs módosítás,'default' az alapértelmezett beállításhoz):"
    CHANGE_PLAYLIST_FOLDER_FORMAT = "Playlist folder format('0'-not modify,'default'-to set default):"
    CHANGE_TRACK_FILE_FORMAT = "Track fájl neve('0' nincs módosítás,'default' az alapértelmezett beállításhoz):"
    CHANGE_VIDEO_FILE_FORMAT = "Video file format('0'-nincs módosítás,'default' az alapértelmezett beállításhoz):"
    CHANGE_SHOW_PROGRESS = "Haladás megjelenítése('0'-Nem, '1'-Igen):"
    CHANGE_SHOW_TRACKINFO = "Track infók megjelenítése('0'-Nem,'1'-Igen):"
    CHANGE_SAVE_ALBUM_INFO = "AlbumInfo.txt mentése('0'-Nem, '1'-Igen):"
    CHANGE_ADD_LYRICS = "Dalszöveg hozzáadása('0'-Nem,'1'-Igen):"
    CHANGE_LYRICS_SERVER_PROXY = "Dalszöveg kiszolgáló proxy('0' nincs módosítás):"
    CHANGE_ADD_LRC_FILE = "Dalszöveg mentése időbélyeggel .lrc fájl('0'-Nem,'1'-Igen):"
    CHANGE_ADD_TYPE_FOLDER = "Mappa típus hozzáadása, pl. Album/Video/Playlist('0'-Nem,'1'-Igen):"
    CHANGE_MULITHREAD_DOWNLOAD = "Többszálas letöltés('0'-Nem,'1'-Igen):"

    # {} are required in these strings
    AUTH_START_LOGIN = "Bejelentkezési folyamat elindítása..."
    AUTH_LOGIN_CODE = "A bejelentkezési kódod {}"
    AUTH_NEXT_STEP = "Menj a {} a következő {} a beállítás befejezéséhez."
    AUTH_WAITING = "Engedélyre várva..."
    AUTH_TIMEOUT = "A művelet leállt."

    MSG_VALID_ACCESSTOKEN = "AccessToken érvényessége {}."
    MSG_INVALID_ACCESSTOKEN = "Lejárt AccessToken. Megpróbálom frissíteni."
    MSG_PATH_ERR = "Az útvonal hibás!"
    MSG_INPUT_ERR = "Beviteli hiba!"

    MODEL_ALBUM_PROPERTY = "ALBUM-INFÓ"
    MODEL_TRACK_PROPERTY = "TRACK-INFÓ"
    MODEL_VIDEO_PROPERTY = "VIDEO-INFÓ"
    MODEL_ARTIST_PROPERTY = "ELŐADÓ-INFÓ"
    MODEL_PLAYLIST_PROPERTY = "LEJÁTSZÁSI LISTA-INFÓ"

    MODEL_TITLE = 'Cím'
    MODEL_TRACK_NUMBER = 'Track száma'
    MODEL_VIDEO_NUMBER = 'Videó száma'
    MODEL_RELEASE_DATE = 'Megjelenés dátuma'
    MODEL_VERSION = 'Verzió'
    MODEL_EXPLICIT = 'Explicit'
    MODEL_ALBUM = 'Album'
    MODEL_ID = 'ID'
    MODEL_NAME = 'Név'
    MODEL_TYPE = 'Típus'
