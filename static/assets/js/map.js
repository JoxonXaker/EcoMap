maptilersdk.config.apiKey = 'OQ1mmfPCY8o0S2GuKYi1';


const map = new maptilersdk.Map({
    container: 'map', // container's id or the HTML element to render the map
    style: "c27e4100-18e0-409b-b694-b29f1cc35082",
    center: [69.3, 41.3], // starting position [lng, lat]
    zoom: 11, // starting zoom
});

let mapFrame = document.getElementById('map')
let body = document.querySelector('body')

map.addControl(new maptilersdk.FullscreenControl({container: mapFrame}));


let setview = document.getElementById('setview')

// aytilgan kordinataga borish
setview.addEventListener("click", (even) => {
    map.fitBounds([[69.28664720912803, 41.34084349253797], [69.28664720912803, 41.34084349253797]], {maxZoom: 16.5})

    console.log([51.505, -0.09])
})


