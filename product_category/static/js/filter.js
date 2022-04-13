$(document).ready(function(){
    $('.seller-category').click(function(event) {
        event.preventDefault()
        let cat = $(this).attr('pid')
        let csrf = $("input[name=csrfmiddlewaretoken]").val()
        console.log(cat);
        $.ajax({
            url: 'seller-category',
            method : 'GET',
            data : {'id':cat},
            success: function(data){
                let category_data = data.data
                console.log(data.data)
                $('.hide').empty()
                    $('.paginater-hide').hide()
                    $('.main').empty()
                    $.each(category_data, function(key, val){
                        console.log(val.name)
                        $(".main").append(`
                        <div class="jumbotron m-5 mt-5 main">
                        <img src="${val.image}" class="image_container" alt="" width="250px" height="250px"> 
                        <h1 class="display-4" id="product_name">${val.name}</h1> 
                        <p class="lead">${val.discription}</p>
                        <hr class="my-4">
                        <p>₹${val.price}</p>
                        <p>${val.category}</p>
                        <p>Quantity : ${val.quantity}</p>
                        <p>${val.user}</p>
                        <a class="btn btn-primary btn-lg" href="/seller-details/${val.id}" role="button">Details</a>   
                        <a class="btn btn-warning btn-lg" href="/edit-product/${val.id}" role="button">Edit</a>
                        <a class="btn btn-danger btn-lg" href="/delete-product/${val.id}" role="button">Delete</a>
                        </div>
                        `)     
                    });
            }
        })
    })
})



$(document).ready(function () {
    $("#sellersearchbtn").click(function (event) {
        event.preventDefault()
        const search = $("#sellersearchinput").val()
        let csrf = $("input[name=csrfmiddlewaretoken]").val()
        $.ajax({
            url: 'seller-search',
            method: 'GET',
            data: {'search': search, 'csrfmiddlewaretoken':csrf},
            success: function (data) {
                let search_data = data.data
                console.log(search_data)
                if(search.length > 0){
                    $('.hide').empty()
                    $('.paginater-hide').empty()
                    $('.main').empty()
                    $.each(search_data, function(key, val){
                        console.log(val.name)
                        $(".main").append(`
                        <div class="jumbotron m-5 mt-5 main">
                        <img src="${val.image}" class="image_container" alt="" width="250px" height="250px"> 
                        <h1 class="display-4" id="product_name">${val.name}</h1> 
                        <p class="lead">${val.discription}</p>
                        <hr class="my-4">
                        <p>₹${val.price}</p>
                        <p>${val.category}</p>
                        <p>Quantity : ${val.quantity}</p>
                        <p>${val.user}</p>
                        <a class="btn btn-primary btn-lg" href="/seller-details/${val.id}" role="button">Details</a>   
                        <a class="btn btn-warning btn-lg" href="/edit-product/${val.id}" role="button">Edit</a>
                        <a class="btn btn-danger btn-lg" href="/delete-product/${val.id}" role="button">Delete</a>
                        </div>
                        `)     
                    });
                }    
            }
        });
    });
});
