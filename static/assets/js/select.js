const region = document.getElementById('region')
const district = document.getElementById('district')
const organization = document.getElementById('organ')


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

region.addEventListener('change', (even) => {
    district.innerHTML = "<option value='' selected disabled hidden>Choose a district &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>"

    districts[even.target.value].forEach((item) => {
        district.innerHTML += "<option value='" + item + "'>" + item + " tumani</option>"
    })

})


district.addEventListener('change', (even) => {
    let organ = "<option value='' selected disabled hidden>Choose an organization&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>"

    $.ajax({
        type: "POST",
        url: "data",
        data: {
            "district": even.target.value,
        },
        header: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrftoken,
        },
        success: function (responce) {
            responce.result.forEach((item) => {
                organ += '<option value="' + item['id'] + '">' + item['name'] + '</option>'
            })
            organization.innerHTML = organ
        },
        error: function () {
            alert('Ulanish nuqtasi bilan muammo bor:(')
        }
    })


})


organization.addEventListener('change', (even) => {
    document.getElementById('js-mainloader').hidden = false

    function cancellationLoader() {
        document.getElementById('js-mainloader').hidden = true
    }

    $.ajax({
        type: "GET",
        url: `data?organ=${even.target.value}`,
        header: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrftoken,
        },
        success: function (responce) {
            // remove old markers
            document.querySelectorAll('.tree-marker-default').forEach(box => {
                box.remove()
            })
            document.querySelectorAll('.organization-marker-default').forEach(box => {
                box.remove()
            })

            // get response by backend
            responce.features.forEach(function (marker) {
                let el = document.createElement('div');

                // make new markers
                if (marker.type === 'tree') {
                    el.className = 'tree-marker-default';
                } else if (marker.type === 'organization') {
                    if (marker.geometry.type === 0) {
                        el.className = 'organization-marker-default';
                        el.style.background = "url('" + marker.properties.icon + "')"
                        el.style.backgroundSize = "cover"
                        el.innerHTML = "<p>" + marker.properties.name + "</p>"
                        map.fitBounds([marker.geometry.coordinates, marker.geometry.coordinates], {maxZoom: 16.5})
                    }
                    let info_Bar_1 = document.getElementById('info_Bar_1')
                    info_Bar_1.querySelector('h6').innerText = 'Tashkilot haqida'
                    info_Bar_1.querySelector('p').innerHTML = `Viloyat: <b>${region.value.toUpperCase()}</b> <br>
                        Tuman: <b>${district.value.toUpperCase()}</b> <br>
                        Nomi: <b>${marker.properties.name}</b> <br>
                        Email: <b>${marker.properties.email}</b> <br>
                        Telefon: <b>${marker.properties.phone}</b> <br>
                        Maydoni: <b>${marker.properties.area}</b> m<sup>2</sup><br>
                        Daraxtlar soni: <b>${marker.properties.count}</b> ta <br>`
                    let info_Bar_2 = document.getElementById('info_Bar_2')
                    info_Bar_2.querySelector('h6').innerText = 'Mas`ul shaxslar'
                    marker.properties.persons.forEach(person => {
                        info_Bar_2.querySelector('p').innerHTML = `
                            Ma'sul: <b>${person.name}</b> <br>
                            Lavozimi: <b>${person.position}</b> <br>
                            Telefon: <b>${person.phone}</b> <br><br>
                            Photo: ${person.img}`
                    })


                }

                // make slide Image
                let i = 1
                marker.properties.img.forEach((image) => {
                    document.getElementById(`image-content-large${i}`).src = image
                    document.getElementById(`image-content-small${i}`).src = image
                    i = i + 1;
                });


                // set markers location
                new maptilersdk.Marker(el)
                    .setLngLat(marker.geometry.coordinates)
                    .addTo(map);

                // click to set slide Image
                el.addEventListener('click', (obj) => {
                    document.getElementById('js-mainloader').hidden = false

                    function cancellation() {
                        document.getElementById('js-mainloader').hidden = true
                    }

                    let i = 1
                    marker.properties.img.forEach((image) => {
                        document.getElementById(`image-content-large${i}`).src = image
                        document.getElementById(`image-content-small${i}`).src = image
                        i = i + 1;
                    })
                    if (marker.type === 'tree') {
                        let info_bar_1 = document.getElementById('info_Bar_1')
                        info_bar_1.querySelector('h6').innerText = 'Daraxt haqida'
                        info_bar_1.querySelector('p').innerHTML =
                            `Nomi: <b>${marker.properties.name}</b> <br>
                             Turi: <b>${marker.properties.type}</b> <br>
                             Bo'yi: <b>${marker.properties.tall}</b> m<br>
                             Daraxt holati: <b>${marker.properties.status}</b><br>
                             Suvli holati: <b>${marker.properties.irrigation}</b><br>
                             Tekshiruv Vaqti:<br><b>${marker.properties.create_date}</b><br>`
                    } else if (marker.type === 'organization') {
                        let info_bar_1 = document.getElementById('info_Bar_1')
                        info_bar_1.querySelector('h6').innerText = 'Tashkilot haqida'
                        info_bar_1.querySelector('p').innerHTML =
                            `Viloyat: <b>${region.value.toUpperCase()}</b> <br>
                             Tuman: <b>${district.value.toUpperCase()}</b> <br>
                             Nomi: <b>${marker.properties.name}</b> <br>
                             Email: <b>${marker.properties.email}</b> <br>
                             Telefon: <b>${marker.properties.phone}</b> <br>
                             Maydoni: <b>${marker.properties.area}</b> m<sup>2</sup><br>
                             Daraxtlar soni: <b>${marker.properties.count}</b> ta <br>`
                    }
                    setTimeout(cancellation, 1000)
                })
            });
        },
        error: function () {
            alert('Ulanish nuqtasi bilan muammo bor:(')
        }
    })

    setTimeout(cancellationLoader, 1000)


})


function setInfoBar() {

}


