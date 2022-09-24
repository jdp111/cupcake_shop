
async function showAll(){
    const allCakes = await axios.get('/api/cupcakes')
    
    const cakeList = allCakes.data.cupcakes
    console.log(cakeList)
    console.log(cakeList[0]["rating"])

    for (const cake of cakeList){
        const cakeHolder = $("<li>").append("<p>").text(`${cake["flavor"]}`)
        $('.cakeList').append(cakeHolder)
    }

}


async function addnew(){
    newFlav = $('#flavor').val()
    newSze = $('#size').val()
    newRtg = $('#rating').val()
    newImg = $('#image').val()

    console.log(newFlav)
    const $params = {'flavor':newFlav, 'size':newSze, 'rating':newRtg, 'image':newImg}
    console.log($params)
    const json = JSON.stringify($params)
    const newCake = await axios.post('/api/cupcakes',$params)
    const cake = newCake.data.cupcake
    console.log(cake)
    const cakeHolder = $("<li>").append("<p>").text(`${cake["flavor"]}`)
    $('.cakeList').append(cakeHolder)

}


$('.new').click(addnew)


showAll()