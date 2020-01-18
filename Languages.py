import os, sys, pprint
# [Optional] Google-translate
try:
    from googletrans import Translator
    googletransInstall = True
except:
    googletransInstall = False

class Languages:

    codes = {
        "Afrikaans": "af",
        "Albanian": "sq",
        "Amharic": "am",
        "Arabic": "ar",
        "Armenian": "hy",
        "Azerbaijani": "az",
        "Basque": "eu",
        "Belarusian": "be",
        "Bengali": "bn",
        "Bosnian": "bs",
        "Bulgarian": "bg",
        "Catalan": "ca",
        "Cebuano": "ceb",
        "Chinese (Simplied)": "zh-CN",
        "Chinese (Traditional)": "zh-TW",
        "Corsican": "co",
        "Croatian": "hr",
        "Czech": "cs",
        "Danish": "da",
        "Dutch": "nl",
        "English": "en",
        "Esperanto": "eo",
        "Estonian": "et",
        "Finnish": "fi",
        "French": "fr",
        "Frisian": "fy",
        "Galician": "gl",
        "Georgian": "ka",
        "German": "de",
        "Greek": "el",
        "Gujarati": "gu",
        "Haitian Creole": "ht",
        "Hausa": "ha",
        "Hawaiian": "haw",
        "Hebrew he or": "iw",
        "Hindi": "hi",
        "Hmong": "hmn",
        "Hungarian": "hu",
        "Icelandic": "is",
        "Igbo": "ig",
        "Indonesian": "id",
        "Irish": "ga",
        "Italian": "it",
        "Japanese": "ja",
        "Javanese": "jv",
        "Kannada": "kn",
        "Kazakh": "kk",
        "Khmer": "km",
        "Korean": "ko",
        "Kurdish": "ku",
        "Kyrgyz": "ky",
        "Lao": "lo",
        "Latin": "la",
        "Latvian": "lv",
        "Lithuanian": "lt",
        "Luxembourgish": "lb",
        "Macedonian": "mk",
        "Malagasy": "mg",
        "Malay": "ms",
        "Malayalam": "ml",
        "Maltese": "mt",
        "Maori": "mi",
        "Marathi": "mr",
        "Mongolian": "mn",
        "Myanmar (Burmese)": "my",
        "Nepali": "ne",
        "Norwegian": "no",
        "Nyanja (Chichewa)": "ny",
        "Pashto": "ps",
        "Persian": "fa",
        "Polish": "pl",
        "Portuguese (Portugal, Brazil)": "pt",
        "Punjabi": "pa",
        "Romanian": "ro",
        "Russian": "ru",
        "Samoan": "sm",
        "Scots Gaelic": "gd",
        "Serbian": "sr",
        "Sesotho": "st",
        "Shona": "sn",
        "Sindhi": "sd",
        "Sinhala (Sinhalese)": "si",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Somali": "so",
        "Spanish": "es",
        "Sundanese": "su",
        "Swahili": "sw",
        "Swedish": "sv",
        "Tagalog (Filipino)": "tl",
        "Tajik": "tg",
        "Tamil": "ta",
        "Telugu": "te",
        "Thai": "th",
        "Turkish": "tr",
        "Ukrainian": "uk",
        "Urdu": "ur",
        "Uzbek": "uz",
        "Vietnamese": "vi",
        "Welsh": "cy",
        "Xhosa": "xh",
        "Yiddish": "yi",
        "Yoruba": "yo",
        "Zulu": "zu",
    }

    interface = {
        "menu1_app": "UniqueBible",
        "menu1_fullScreen": "Full Screen",
        "menu1_resize": "Resize",
        "menu1_topHalf": "Top Half",
        "menu1_leftHalf": "Left Half",
        "menu1_remoteControl": "Remote Control [On / Off]",
        "menu1_setDefaultFont": "Set Default Font and Size",
        "menu1_setChineseFont": "Set Chinese Font",
        "menu1_setAbbreviations": "Set Bible Abbreviations",
        "menu1_setMyLanguage": "Set my Language",
        "menu1_setMyFavouriteBible": "Set my Favourite Bible",
        "menu1_wikiPages": "Wiki Pages",
        "menu1_update": "Update",
        "menu2_view": "View",
        "menu2_all": "All Toolbars [Show / Hide]",
        "menu2_topOnly": "All Toolbars / Top Toolbar Only",
        "menu2_top": "Top Toolbar [Show / Hide]",
        "menu2_second": "Second Toolbar [Show / Hide]",
        "menu2_left": "Left Toolbar [Show / Hide]",
        "menu2_right": "Right Toolbar [Show / Hide]",
        "menu2_icons": "Toolbar Icons [Full-size / Standard]",
        "menu2_landscape": "Landscape / Portrait Mode",
        "menu2_study": "Study View [Resize / Hide]",
        "menu2_bottom": "Bottom View [Show / Hide]",
        "menu2_hover": "Hovering feature [Enable / Disable]",
        "menu2_larger": "Larger Font",
        "menu2_smaller": "Smaller Font",
        "menu2_format": "Formatted / Plain Bibles",
        "menu2_subHeadings": "Add Sub-headings to Plain Bibles",
        "menu3_history": "History",
        "menu3_main": "Main",
        "menu3_mainBack": "Back",
        "menu3_mainForward": "Forward",
        "menu3_study": "Study",
        "menu3_studyBack": "Back",
        "menu3_studyForward": "Forward",
        "menu4_further": "Further Study",
        "menu4_next": "Next Chapter",
        "menu4_previous": "Previous Chapter",
        "menu4_indexes": "Smart Indexes",
        "menu4_commentary": "Commentary",
        "menu4_traslations": "Translations",
        "menu4_discourse": "Discourse",
        "menu4_words": "Words",
        "menu4_tdw": "TDW Combo",
        "menu4_crossRef": "Cross References",
        "menu4_tske": "TSK (Enhanced)",
        "menu4_compareAll": "Compare All Versions",
        "menu4_compare": "Compare with ...",
        "menu4_parallel": "Parallel with ...",
        "menu5_search": "Search",
        "menu5_bible": "Bible / Bibles",
        "menu5_main": "Last Opened Bible on Main View",
        "menu5_study": "Last Opened Bible on Study View",
        "menu5_dictionary": "Last Opened Dictionary",
        "menu5_encyclopedia": "Last Opened Encyclopedia",
        "menu5_book": "Last Opened Book",
        "menu5_characters": "Bible Charcters",
        "menu5_names": "Bible Names",
        "menu5_locations": "Bible Locations",
        "menu5_topics": "Bible Topics",
        "menu5_lexicon": "Hebrew / Greek Lexicons",
        "menu5_3rdDict": "Third Party Dictionaries",
        "menu6_notes": "Notes",
        "menu6_mainChapter": "Note on Main Chapter",
        "menu6_studyChapter": "Note on Study Chapter",
        "menu6_searchChapters": "Search Notes on Chapters",
        "menu6_mainVerse": "Note on Main Verse",
        "menu6_studyVerse": "Note on Study Verse",
        "menu6_searchVerses": "Search Notes on Verses",
        "menu7_topics": "Topics",
        "menu7_create": "Create a Topical Note",
        "menu7_open": "Open Note Files",
        "menu7_recent": "Recent Files",
        "menu7_read": "Read Last Opened File",
        "menu7_edit": "Edit Last Opened File",
        "menu7_paste": "Paste from Clipboard",
        "menu8_resources": "Resources",
        "menu8_bibles": "Install Formatted Bibles",
        "menu8_commentaries": "Install Bible Commentaries",
        "menu8_datasets": "Install Marvel.bible Datasets",
        "menu8_plusLexicons": "Import BibleBento Plus Lexicons in a Folder",
        "menu8_plusDictionaries": "Import BibleBento Plus Dictionaries in a Folder",
        "menu8_3rdParty": "Import 3rd Party Modules",
        "menu8_3rdPartyInFolder": "Import Supported 3rd Party Modules in a Folder",
        "menu8_settings": "Import Settings",
        "menu8_tagFile": "Tag References in a File",
        "menu8_tagFiles": "Tag References in Multiple Files",
        "menu8_tagFolder": "Tag References in All Files of a Folder",
        "menu9_information": "Information",
        "menu9_credits": "Credits",
        "menu9_contact": "Contact Eliran Wong",
    }

    def translateInterfaceIntoAllLanguages(self):
        if googletransInstall:
            for code in self.codes.values():
                print("translating '{0}' interface ...".format(code))
                translator = Translator()
                tempDict = {}
                for key, value in self.interface.items():
                    tempDict[key] = value
#                    try:
#                        tempDict[key] = translator.translate(value, dest=code).text
#                    except:
#                        tempDict[key] = value
                with open("interface.py", "a") as fileObj:
                    code = code.replace("-", "")
                    fileObj.write("\n\nuB{0} = {1}".format(code, pprint.pformat(tempDict)))


if __name__ == '__main__':
    Languages().translateInterfaceIntoAllLanguages()
    
    
    
