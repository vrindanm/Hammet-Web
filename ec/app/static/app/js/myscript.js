// $('.plus-cart').click(function(){
//     var id = $(this).attr("pid").toString();
//     var size = $('#size').val();  // Get the selected size
//     var eml = this.parentNode.children[2];
    
//     $.ajax({
//         type: "GET",
//         url: "/add-to-cart/",  // Update the URL to match the view name
//         data: {
//             prod_id: id,
//             size: size  // Pass the selected size as a parameter
//         },
//         success: function(data) {
//             console.log("data =", data);
//             eml.innerText = data.quantity;
//             document.getElementById("amount").innerText = data.amount;
//             document.getElementById("totalamount").innerText = data.totalamount;
//         }
//     });
// });





$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2]
    console.log("pid = " ,id)
    $.ajax({
    type:"GET",
    url:"/pluscart",
    data:{
        prod_id:id
    },
    success:function(data){
        console.log("data=",data);
        eml.innerText=data.quantity
        document.getElementById("amount").innerText=data.amount 
        document.getElementById("totalamount").innerText=data.totalamount 
    }
    })    
}) 

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2]
    console.log("pid = " ,id)
    $.ajax({
    type:"GET",
    url:"/minuscart",
    data:{
        prod_id:id
    },
    success:function(data){
        console.log("data=",data);
        eml.innerText=data.quantity
        document.getElementById("amount").innerText=data.amount 
        document.getElementById("totalamount").innerText=data.totalamount 
    }
    })    
})     

$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    console.log("pid = " ,id)
    $.ajax({
    type:"GET",
    url:"/removecart",
    data:{
        prod_id:id
    },
    success:function(data){
        console.log("data=",data);
        document.getElementById("amount").innerText=data.amount 
        document.getElementById("totalamount").innerText=data.totalamount 
        eml.parentNode.parentNode.parentNode.parentNode.remove() 
    }
    })    
})   

$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/pluswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            //alert(data.message)
            window.location.href = `http://localhost:8000/product-detail/${id}`
        }
    })
})


$('.minus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/minuswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            window.location.href = `http://localhost:8000/product-detail/${id}`
        }
    })
})
 

// $.ajax({
//     url: '/plus_cart/',
//     data: {
//         'prod_id': product_id
//     },
//     dataType: 'json',
//     success: function(response) {
        
//         if (response.hasOwnProperty('message')) {
//             // Display the out-of-stock message
//             console.log(response.message);
//         } else {
//             // Process the successful response and update the UI
//             var quantity = response.quantity;
//             var amount = response.amount;
//             var totalamount = response.totalamount;

//             // Update the UI with the retrieved values
//             // ...
//         }
//     },
//     error: function(xhr, textStatus, error) {
//         console.log(error);  // Log any potential error
//     }
// });

$.ajax({
    url: '/plus_cart/',
    data: {
        'prod_id': product_id
    },
    dataType: 'json',
    success: function(response) {
        if (response.hasOwnProperty('message')) {
            // Display the out-of-stock message
            var messageContainer = document.getElementById('message-container');
            messageContainer.textContent = response.message;
        } else {
            // Process the successful response and update the UI
            var quantity = response.quantity;
            var amount = response.amount;
            var totalamount = response.totalamount;

            // Update the UI with the retrieved values
            // ...
        }
    },
    error: function(xhr, textStatus, error) {
        console.log(error);  // Log any potential error
    }
});






    // var id=$(this).attr("pid").toString();
    // var eml=this.parentNode.children[2] 
    // console.log("pid=",id) 
    // $.ajax({
    //     type:"GET",
    //     url:"/pluscart",
    //     data:{
    //         prod_id:id
    //     },
    //     success:function(data){
    //         console.log("data=",data);
    //         eml.innerText=data.quantity
    //         document.getElementById("amount").innerText=data.amount 
    //         document.getElementById("totalamount").innerText=data.totalamount 
    //     }      
    // })


// $('.minus-cart').click(function(){
//     console.log("minus button clicked")  
// })  

 

// $('.minus-cart').click(function(){
//     var id=$(this).attr("pid").toString();
//     var eml=this
//     $.ajax({
//         type:"GET",
//         url:"/minuscart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             eml.innerText=data.quantity
//             document.getElementById("amount").innerText=data.amount 
//             document.getElementById("totalamount").innerText=data.totalamount 
//             eml.parentNode.parentNode.parentNode.parentNode.parentNode.remove()
//         }      
//     })
// })

// $('.remove-cart').click(function(){
//     var id=$(this).attr("pid").toString();
//     var eml=this
//     $.ajax({
//         type:"GET",
//         url:"/removecart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             document.getElementById("amount").innerText=data.amount 
//             document.getElementById("totalamount").innerText=data.totalamount 
//             eml.parentNode.parentNode.parentNode.parentNode.parentNode.remove()
//         }      
//     })
// })

// $('#slider1, #slider2, #slider3').owlCarousel({
//     loop: true,
//     margin: 20,
//     responsiveClass: true,
//     responsive: {
//         0: {
//             items: 2,
//             nav: false,
//             autoplay: true,
//         },
//         600: {
//             items: 4,
//             nav: true,
//             autoplay: true,
//         },
//         1000: {
//             items: 6,
//             nav: true,
//             loop: true,
//             autoplay: true,
//         }
//     }
// })

// $('.plus-cart').click(function(){
//     var id=$(this).attr("pid").toString();
//     var eml=this.parentNode.children[2] 
//     $.ajax({
//         type:"GET",
//         url:"/pluscart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             eml.innerText=data.quantity 
//             document.getElementById("amount").innerText=data.amount 
//             document.getElementById("totalamount").innerText=data.totalamount
//         }
//     })
// })

// $('.minus-cart').click(function(){
//     var id=$(this).attr("pid").toString();
//     var eml=this.parentNode.children[2] 
//     $.ajax({
//         type:"GET",
//         url:"/minuscart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             eml.innerText=data.quantity 
//             document.getElementById("amount").innerText=data.amount 
//             document.getElementById("totalamount").innerText=data.totalamount
//         }
//     })
// })


// $('.remove-cart').click(function(){
//     var id=$(this).attr("pid").toString();
//     var eml=this
//     $.ajax({
//         type:"GET",
//         url:"/removecart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             document.getElementById("amount").innerText=data.amount 
//             document.getElementById("totalamount").innerText=data.totalamount
//             eml.parentNode.parentNode.parentNode.parentNode.remove() 
//         }
//     })
// })


// $('.plus-wishlist').click(function(){
//     var id=$(this).attr("pid").toString();
//     $.ajax({
//         type:"GET",
//         url:"/pluswishlist",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             //alert(data.message)
//             window.location.href = `http://localhost:8000/product-detail/${id}`
//         }
//     })
// })


// $('.minus-wishlist').click(function(){
//     var id=$(this).attr("pid").toString();
//     $.ajax({
//         type:"GET",
//         url:"/minuswishlist",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             window.location.href = `http://localhost:8000/product-detail/${id}`
//         }
//     })
// })


