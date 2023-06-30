const districts = {
    'tashkent': ['Chilonzor', 'Mirobod', 'Mirzo Ulug`bek', 'Olmazor', 'Sergeli', 'Shayxontohur', 'Uchtepa', 'Yakkasaroy', 'Yangihayot', 'Yashnobod', 'Yunusobod',],
    'tashkentv': ['Bekobod', 'Boʻka', 'Boʻstonliq', 'Zangiota', 'Oqqoʻrgʻon', 'Ohangaron', 'Parkent', 'Piskent', 'Chinoz', 'Yuqori Chirchiq', 'Yangiyoʻl', 'Oʻrta Chirchiq', 'Qibray', 'Quyi Chirchiq'],
    "andijan": ["Andijan", "Asaka", "Bo`z", "Buloqboshi", "Izboskan", "Jalalkuduk", "Marhamat", "Oltinkan", "Paxtaobod", "Qorasuv", "Shahrixon", "Ulug`nor", "Xonobod"],
    "bukhara": ["Alat", "Bukhara", "G`ijduvon", "Jondor", "Karakul", "Kogon", "Olot", "Peshku", "Romitan", "Shofirkon", "Vabkent"],
    "fergana": ["Bag`dod ", "Beshariq ", "Buvayda ", "Dang`ara ", "Farg`ona ", "Furqat ", "Qo`qon ", "Qo`rg`ontepa ", "Quva ", "Rishton ", "So`x ", "Toshloq ", "Uchqo`rg`on", "Yozyovon"],
    "jizzakh": ["Arnasoy", "Baxmal", "Chiroqchi", "Dustlik", "Forish", "G`allaorol", "Jizzax", "Mirzacho`l", "Pakhtakor", "Yangiabad", "Zarbdor", "Zafarobod "],
    "qashkadarya": ["Chirakchi", "Dehkanabad", "G‘uzor", "Kasbi", "Kitob", "Mirishkor", "Muborak", "Nishon", "Qamashi", "Qarshi", "Shakhrisabz", "Shahrisabz", "Shirin", "Yakkabog‘", "Yakkabog'"],
    "namangan": ["Chortoq", "Chust", "Dexqonobod", "Kosonsoy", "Mingbuloq", "Namangan", "Norin", "Pop", "To`raqo`rg`on", "Uychi", "Uygen", "Yangiobod"],
    "navoiy": ["Kiziltepa", "Konimex", "Navoiy", "Nurota", "Tomdi", "Uchkuduk", "Xatirchi", "Zarafshon", "Navbahor"],
    "samarqant": ["Bulungur", "Ishtikhon", "Jambay", "Katta-Kurgan", "Narpay", "Nurobod", "Oqdaryo", "Pakhtachi", "Pastdarg‘om", "Payariq", "Samarqand", "Toyloq", "Urgut", "Yangiyer", "Yoson", "Yoshlar"],
    "surxondaryo": ["Angor", "Boysun", "Denov", "Jarqo‘rg‘on", "Qiziriq", "Muzrabot", "Oltinsoy", "Qumqo‘rg‘on", "Sariosiyo", "Sherobod", "Sho‘rchi", "Termiz", "Uzun", "Qiziltepa"],
    "sirdaryo": ["Boyovut", "Gulistan", "Mirzachul", "Ohangaron", "Saykhunobod", "Sardoba", "Sharof Rashidov", "Yangi", "Yaypan"],
    "xorazm": ["Bog‘ot", "Gurlan", "Khiva", "O‘zun", "Qo‘shko‘pir", "Shavat", "Urganch", "Xonqa", "Yangiariq", "Yangibozor", "Yangiyer"],
    'qoraqalpoq': ["Beruniy", "Chimboy", "Ellikqal'a", "Kegeyli", "Mo‘ynoq", "Nukus", "Qanliko‘l", "Qo‘ng‘irot", "Qorao‘zak", "Shumanay", "Taxiatosh", "To‘rtko‘l", "Xojeli"]
}


window.addEventListener("load", function () {
    let region_admin = document.getElementById('id_region')

    let district_admin = document.getElementById('id_district')
    district_admin.innerHTML = "<option value='' selected disabled hidden>Choose a district &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>"
    region_admin.innerHTML += "<option value='' selected disabled hidden>Choose a region &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>"


    region_admin.addEventListener('change', (even) => {
        district_admin.innerHTML = "<option value='' selected disabled hidden>Choose a district &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>"
        districts[even.target.value].forEach((item) => {
            district_admin.innerHTML += "<option value='" + item + "'>" + item + " tumani</option>"
        })

    })


});

