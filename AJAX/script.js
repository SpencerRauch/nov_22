console.log("Script linked")
const URL = "https://pokeapi.co/api/v2/pokemon/"

function getPoke(event){
    event.preventDefault()
    console.log("submitted")
    const pokeResultDiv = document.querySelector("#pokeResult")
    const pokeName = document.querySelector("#pokeName").value
    console.log(pokeName)
    pokeResultDiv.innerHTML = "Loading......"
    fetch(URL + pokeName)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            pokeResultDiv.innerHTML = `
            <h3> Number ${data.id} ${data.name} <h3>
            <img src="${data.sprites.front_default}">
            <h4>Types:</h4>
            `
            for (let type of data.types ){
                console.log(type.type.name)
                pokeResultDiv.innerHTML += `
                <p>${type.type.name}</p>
                `
            }
        })
        .catch(err => console.log(err))
}

async function randPoke(event) {
    event.preventDefault()
    console.log("random linked")
    const pokeResultDiv = document.querySelector("#pokeResult")
    let rand = Math.floor(Math.random() * 900);
    let response = await fetch(URL + rand)
    let data = await response.json()
    pokeResultDiv.innerHTML = `
    <h3> Number ${data.id} ${data.name} <h3>
    <img src="${data.sprites.front_default}">
    <h4>Types:</h4>
    `
    for (let type of data.types ){
        console.log(type.type.name)
        pokeResultDiv.innerHTML += `
        <p>${type.type.name}</p>
        `
    }
}