# Copyright (C) 2005-2006 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# Gaupol is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaupol; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA 02110-1301, USA.


"""Names and codes for languages, countries and locales.

Module variables:

    COUNTRIES: Dictionary mapping ISO 3166 codes to country names
    LANGS:     Dictionary mapping ISO 639 codes to language names
    LOCALES:   Frozen set of locale codes

Language codes are ISO 639 two-letter codes. Country codes are ISO 3166 codes.
These combined with an underscore form locale codes. Translations for the
language and country names are acquired from the 'iso-codes' gettext domain if
it exists.
"""

# Lists of languages and countries have been generated from iso-codes [1]
# project's XML files iso_639.xml and iso_3166.xml with copyrights
#
# Copyright (C) 2005 Alastair McKinstry <mckinstry@computer.org>
# Copyright (C) 2002,2006 Alastair McKinstry <mckinstry@debian.org>
#
# List of locales has been gathered from lists by AbiWord [2] and
# OpenOffice [3]. Additionally, two-letter versions of each locale have been
# added.
#
# [1] http://pkg-isocodes.alioth.debian.org/
# [2] http://www.abisource.com/lxr/source/abi/src/af/util/xp/ut_Language.cpp
# [3] http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/available.lst

# pylint: disable-msg=C0301


from gettext import dgettext
from gettext import gettext as _


COUNTRIES = {
    "AD": "Andorra",
    "AE": "United Arab Emirates",
    "AF": "Afghanistan",
    "AG": "Antigua and Barbuda",
    "AI": "Anguilla",
    "AL": "Albania",
    "AM": "Armenia",
    "AN": "Netherlands Antilles",
    "AO": "Angola",
    "AQ": "Antarctica",
    "AR": "Argentina",
    "AS": "American Samoa",
    "AT": "Austria",
    "AU": "Australia",
    "AW": "Aruba",
    "AX": "\303\205land Islands",
    "AZ": "Azerbaijan",
    "BA": "Bosnia and Herzegovina",
    "BB": "Barbados",
    "BD": "Bangladesh",
    "BE": "Belgium",
    "BF": "Burkina Faso",
    "BG": "Bulgaria",
    "BH": "Bahrain",
    "BI": "Burundi",
    "BJ": "Benin",
    "BM": "Bermuda",
    "BN": "Brunei Darussalam",
    "BO": "Bolivia",
    "BR": "Brazil",
    "BS": "Bahamas",
    "BT": "Bhutan",
    "BV": "Bouvet Island",
    "BW": "Botswana",
    "BY": "Belarus",
    "BZ": "Belize",
    "CA": "Canada",
    "CC": "Cocos (Keeling) Islands",
    "CD": "Congo, The Democratic Republic of the",
    "CF": "Central African Republic",
    "CG": "Congo",
    "CH": "Switzerland",
    "CI": "C\303\264te d'Ivoire",
    "CK": "Cook Islands",
    "CL": "Chile",
    "CM": "Cameroon",
    "CN": "China",
    "CO": "Colombia",
    "CR": "Costa Rica",
    "CS": "Serbia and Montenegro",
    "CU": "Cuba",
    "CV": "Cape Verde",
    "CX": "Christmas Island",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DE": "Germany",
    "DJ": "Djibouti",
    "DK": "Denmark",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "DZ": "Algeria",
    "EC": "Ecuador",
    "EE": "Estonia",
    "EG": "Egypt",
    "EH": "Western Sahara",
    "ER": "Eritrea",
    "ES": "Spain",
    "ET": "Ethiopia",
    "FI": "Finland",
    "FJ": "Fiji",
    "FK": "Falkland Islands (Malvinas)",
    "FM": "Micronesia, Federated States of",
    "FO": "Faroe Islands",
    "FR": "France",
    "GA": "Gabon",
    "GB": "United Kingdom",
    "GD": "Grenada",
    "GE": "Georgia",
    "GF": "French Guiana",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GL": "Greenland",
    "GM": "Gambia",
    "GN": "Guinea",
    "GP": "Guadeloupe",
    "GQ": "Equatorial Guinea",
    "GR": "Greece",
    "GS": "South Georgia and the South Sandwich Islands",
    "GT": "Guatemala",
    "GU": "Guam",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HK": "Hong Kong",
    "HM": "Heard Island and McDonald Islands",
    "HN": "Honduras",
    "HR": "Croatia",
    "HT": "Haiti",
    "HU": "Hungary",
    "ID": "Indonesia",
    "IE": "Ireland",
    "IL": "Israel",
    "IN": "India",
    "IO": "British Indian Ocean Territory",
    "IQ": "Iraq",
    "IR": "Iran, Islamic Republic of",
    "IS": "Iceland",
    "IT": "Italy",
    "JM": "Jamaica",
    "JO": "Jordan",
    "JP": "Japan",
    "KE": "Kenya",
    "KG": "Kyrgyzstan",
    "KH": "Cambodia",
    "KI": "Kiribati",
    "KM": "Comoros",
    "KN": "Saint Kitts and Nevis",
    "KP": "Korea, Democratic People's Republic of",
    "KR": "Korea, Republic of",
    "KW": "Kuwait",
    "KY": "Cayman Islands",
    "KZ": "Kazakhstan",
    "LA": "Lao People's Democratic Republic",
    "LB": "Lebanon",
    "LC": "Saint Lucia",
    "LI": "Liechtenstein",
    "LK": "Sri Lanka",
    "LR": "Liberia",
    "LS": "Lesotho",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "LY": "Libyan Arab Jamahiriya",
    "MA": "Morocco",
    "MC": "Monaco",
    "MD": "Moldova, Republic of",
    "MG": "Madagascar",
    "MH": "Marshall Islands",
    "MK": "Macedonia, Republic of",
    "ML": "Mali",
    "MM": "Myanmar",
    "MN": "Mongolia",
    "MO": "Macao",
    "MP": "Northern Mariana Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MS": "Montserrat",
    "MT": "Malta",
    "MU": "Mauritius",
    "MV": "Maldives",
    "MW": "Malawi",
    "MX": "Mexico",
    "MY": "Malaysia",
    "MZ": "Mozambique",
    "NA": "Namibia",
    "NC": "New Caledonia",
    "NE": "Niger",
    "NF": "Norfolk Island",
    "NG": "Nigeria",
    "NI": "Nicaragua",
    "NL": "Netherlands",
    "NO": "Norway",
    "NP": "Nepal",
    "NR": "Nauru",
    "NU": "Niue",
    "NZ": "New Zealand",
    "OM": "Oman",
    "PA": "Panama",
    "PE": "Peru",
    "PF": "French Polynesia",
    "PG": "Papua New Guinea",
    "PH": "Philippines",
    "PK": "Pakistan",
    "PL": "Poland",
    "PM": "Saint Pierre and Miquelon",
    "PN": "Pitcairn",
    "PR": "Puerto Rico",
    "PS": "Palestinian Territory, Occupied",
    "PT": "Portugal",
    "PW": "Palau",
    "PY": "Paraguay",
    "QA": "Qatar",
    "RE": "Reunion",
    "RO": "Romania",
    "RU": "Russian Federation",
    "RW": "Rwanda",
    "SA": "Saudi Arabia",
    "SB": "Solomon Islands",
    "SC": "Seychelles",
    "SD": "Sudan",
    "SE": "Sweden",
    "SG": "Singapore",
    "SH": "Saint Helena",
    "SI": "Slovenia",
    "SJ": "Svalbard and Jan Mayen",
    "SK": "Slovakia",
    "SL": "Sierra Leone",
    "SM": "San Marino",
    "SN": "Senegal",
    "SO": "Somalia",
    "SR": "Suriname",
    "ST": "Sao Tome and Principe",
    "SV": "El Salvador",
    "SY": "Syrian Arab Republic",
    "SZ": "Swaziland",
    "TC": "Turks and Caicos Islands",
    "TD": "Chad",
    "TF": "French Southern Territories",
    "TG": "Togo",
    "TH": "Thailand",
    "TJ": "Tajikistan",
    "TK": "Tokelau",
    "TL": "Timor-Leste",
    "TM": "Turkmenistan",
    "TN": "Tunisia",
    "TO": "Tonga",
    "TR": "Turkey",
    "TT": "Trinidad and Tobago",
    "TV": "Tuvalu",
    "TW": "Taiwan",
    "TZ": "Tanzania, United Republic of",
    "UA": "Ukraine",
    "UG": "Uganda",
    "UM": "United States Minor Outlying Islands",
    "US": "United States",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VA": "Holy See (Vatican City State)",
    "VC": "Saint Vincent and the Grenadines",
    "VE": "Venezuela",
    "VG": "Virgin Islands, British",
    "VI": "Virgin Islands, U.S.",
    "VN": "Viet Nam",
    "VU": "Vanuatu",
    "WF": "Wallis and Futuna",
    "WS": "Samoa",
    "YE": "Yemen",
    "YT": "Mayotte",
    "ZA": "South Africa",
    "ZM": "Zambia",
    "ZW": "Zimbabwe",}

LANGS = {
    "aa": "Afar",
    "ab": "Abkhazian",
    "ae": "Avestan",
    "af": "Afrikaans",
    "ak": "Akan",
    "am": "Amharic",
    "an": "Aragonese",
    "ar": "Arabic",
    "as": "Assamese",
    "av": "Avaric",
    "ay": "Aymara",
    "az": "Azerbaijani",
    "ba": "Bashkir",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bh": "Bihari",
    "bi": "Bislama",
    "bm": "Bambara",
    "bn": "Bengali",
    "bo": "Tibetan",
    "br": "Breton",
    "bs": "Bosnian",
    "ca": "Catalan",
    "ce": "Chechen",
    "ch": "Chamorro",
    "co": "Corsican",
    "cr": "Cree",
    "cs": "Czech",
    "cv": "Chuvash",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "dv": "Divehi",
    "dz": "Dzongkha",
    "ee": "Ewe",
    "el": "Greek, Modern (1453-)",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "ff": "Fulah",
    "fi": "Finnish",
    "fj": "Fijian",
    "fo": "Faroese",
    "fr": "French",
    "fy": "Frisian",
    "ga": "Irish",
    "gd": "Gaelic; Scottish",
    "gl": "Gallegan",
    "gn": "Guarani",
    "gu": "Gujarati",
    "gv": "Manx",
    "ha": "Hausa",
    "he": "Hebrew",
    "hi": "Hindi",
    "ho": "Hiri",
    "hr": "Croatian",
    "ht": "Haitian; Haitian Creole",
    "hu": "Hungarian",
    "hy": "Armenian",
    "hz": "Herero",
    "ia": "Interlingua",
    "id": "Indonesian",
    "ie": "Interlingue",
    "ig": "Igbo",
    "ii": "Sichuan Yi",
    "ik": "Inupiaq",
    "io": "Ido",
    "is": "Icelandic",
    "it": "Italian",
    "iu": "Inuktitut",
    "ja": "Japanese",
    "jv": "Javanese",
    "ka": "Georgian",
    "kg": "Kongo",
    "ki": "Kikuyu",
    "kj": "Kuanyama",
    "kk": "Kazakh",
    "kl": "Greenlandic (Kalaallisut)",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "kr": "Kanuri",
    "ks": "Kashmiri",
    "ku": "Kurdish",
    "kv": "Komi",
    "kw": "Cornish",
    "ky": "Kirghiz",
    "la": "Latin",
    "lb": "Luxembourgish",
    "lg": "Ganda",
    "li": "Limburgian",
    "ln": "Lingala",
    "lo": "Lao",
    "lt": "Lithuanian",
    "lu": "Luba-Katanga",
    "lv": "Latvian",
    "mg": "Malagasy",
    "mh": "Marshallese",
    "mi": "Maori",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mn": "Mongolian",
    "mo": "Moldavian",
    "mr": "Marathi",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "na": "Nauru",
    "nb": "Bokm\303\245l, Norwegian",
    "nd": "Ndebele, North",
    "ne": "Nepali",
    "ng": "Ndonga",
    "nl": "Dutch",
    "nn": "Norwegian Nynorsk",
    "no": "Norwegian",
    "nr": "Ndebele, South",
    "nv": "Navaho",
    "ny": "Chewa; Chichewa; Nyanja",
    "oc": "Occitan (post 1500)",
    "oj": "Ojibwa",
    "om": "Oromo",
    "or": "Oriya",
    "os": "Ossetian",
    "pa": "Punjabi",
    "pi": "Pali",
    "pl": "Polish",
    "ps": "Pushto",
    "pt": "Portuguese",
    "qu": "Quechua",
    "rm": "Raeto-Romance",
    "rn": "Rundi",
    "ro": "Romanian",
    "ru": "Russian",
    "rw": "Kinyarwanda",
    "sa": "Sanskrit",
    "sc": "Sardinian",
    "sd": "Sindhi",
    "se": "Northern Sami",
    "sg": "Sango",
    "si": "Sinhala; Sinhalese",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sm": "Samoan",
    "sn": "Shona",
    "so": "Somali",
    "sq": "Albanian",
    "sr": "Serbian",
    "ss": "Swati",
    "st": "Sotho, Southern",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "tg": "Tajik",
    "th": "Thai",
    "ti": "Tigrinya",
    "tk": "Turkmen",
    "tl": "Tagalog",
    "tn": "Tswana",
    "to": "Tonga (Tonga Islands)",
    "tr": "Turkish",
    "ts": "Tsonga",
    "tt": "Tatar",
    "tw": "Twi",
    "ty": "Tahitian",
    "ug": "Uighur",
    "uk": "Ukrainian",
    "uz": "Uzbek",
    "ve": "Venda",
    "vi": "Vietnamese",
    "vo": "Volapuk",
    "wa": "Walloon",
    "wo": "Wolof",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "za": "Chuang; Zhuang",
    "zh": "Chinese",
    "zu": "Zulu",}

LOCALES = frozenset((
    "af",
    "af_ZA",
    "ak",
    "ak_GH",
    "am",
    "am_ET",
    "ar",
    "ar_EG",
    "ar_SA",
    "as",
    "as_IN",
    "be",
    "be_BY",
    "bg",
    "bg_BG",
    "bn",
    "bn_IN",
    "br",
    "br_FR",
    "ca",
    "ca_ES",
    "co",
    "co_FR",
    "cs",
    "cs_CZ",
    "cy",
    "cy_GB",
    "da",
    "da_DK",
    "de",
    "de_AT",
    "de_CH",
    "de_DE",
    "el",
    "el_GR",
    "en",
    "en_AU",
    "en_CA",
    "en_GB",
    "en_IE",
    "en_NZ",
    "en_US",
    "en_ZA",
    "eo",
    "es",
    "es_AR",
    "es_BO",
    "es_CL",
    "es_CO",
    "es_CR",
    "es_CU",
    "es_DO",
    "es_EC",
    "es_ES",
    "es_GT",
    "es_HN",
    "es_MX",
    "es_NI",
    "es_PA",
    "es_PE",
    "es_PR",
    "es_PY",
    "es_SV",
    "es_UY",
    "es_VE",
    "et",
    "et_EE",
    "eu",
    "eu_ES",
    "fa",
    "fa_IR",
    "fi",
    "fi_FI",
    "fo",
    "fo_FO",
    "fr",
    "fr_BE",
    "fr_CA",
    "fr_CH",
    "fr_FR",
    "fy",
    "fy_NL",
    "ga",
    "ga_IE",
    "gd",
    "gd_GB",
    "gl",
    "gl_ES",
    "ha",
    "ha_NE",
    "ha_NG",
    "he",
    "he_IL",
    "hi",
    "hi_IN",
    "hr",
    "hr_HR",
    "hu",
    "hu_HU",
    "hy",
    "hy_AM",
    "ia",
    "id",
    "id_ID",
    "is",
    "is_IS",
    "it",
    "it_IT",
    "iu",
    "iu_CA",
    "ja",
    "ja_JP",
    "ka",
    "ka_GE",
    "kn",
    "kn_IN",
    "ko",
    "ko_KR",
    "ku",
    "ku_TR",
    "kw",
    "kw_GB",
    "la",
    "la_IT",
    "lo",
    "lo_LA",
    "lt",
    "lt_LT",
    "lv",
    "lv_LV",
    "mg",
    "mg_MG",
    "mh",
    "mh_MH",
    "mh_NR",
    "mi",
    "mi_NZ",
    "mk",
    "mn",
    "mn_MN",
    "mr",
    "mr_IN",
    "ms",
    "ms_MY",
    "nb",
    "nb_NO",
    "nl",
    "nl_BE",
    "nl_NL",
    "nn",
    "nn_NO",
    "no",
    "no_NO",
    "ny",
    "ny_MW",
    "oc",
    "oc_FR",
    "pa",
    "pa_IN",
    "pa_PK",
    "pl",
    "pl_PL",
    "pt",
    "pt_BR",
    "pt_PT",
    "qu",
    "qu_BO",
    "ro",
    "ro_RO",
    "ru",
    "ru_RU",
    "rw",
    "rw_RW",
    "sc",
    "sc_IT",
    "sk",
    "sk_SK",
    "sl",
    "sl_SI",
    "sq",
    "sq_AL",
    "sr",
    "sv",
    "sv_SE",
    "sw",
    "sw_KE",
    "ta",
    "ta_IN",
    "te",
    "te_IN",
    "th",
    "th_TH",
    "tl",
    "tl_PH",
    "tn",
    "tn_ZA",
    "tr",
    "tr_TR",
    "uk",
    "uk_UA",
    "uz",
    "uz_UZ",
    "vi",
    "vi_VN",
    "yi",
    "zh",
    "zh_CN",
    "zh_HK",
    "zh_SG",
    "zh_TW",
    "zu",
    "zu_ZA",))


def get_country(locale):
    """Get the localized country name from locale code or None.

    Raise KeyError if language not found.
    """
    if len(locale) == 5:
        return dgettext("iso_3166", COUNTRIES[locale[3:]])
    return None

def get_language(locale):
    """Get the localized language name from locale code.

    Raise KeyError if language not found.
    """
    return dgettext("iso_639", LANGS[locale[:2]])

def get_long_name(locale):
    """Get the localized long name from locale code.

    Raise KeyError if language not found.
    Return 'Language (Country)'.
    """
    lang = get_language(locale)
    country = get_country(locale)
    if country is not None:
        fields = {"language": lang, "country": country}
        return _("%(language)s (%(country)s)") % fields
    return lang
