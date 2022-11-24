
var input, filter, table, tr, td, i, jb;
table = document.getElementById("table");  
tr = table.getElementsByTagName("tr");

setInterval(function() {
   $('#web-name').effect('bounce',3000)
}, 2000);

$("#search").click(function(){
 $("#search").css("border-color", "grey");  
});

$(".table").append("<tr><td><a href='#'>Cognizant</a></td><td>Developer</td><td>Fulltime</td><td>1000</td><td>22-07-2007</td><td><button class='btn-primary apply'>Apply</button></td></tr>");

$(".table").append("<tr><td><a href='#'>Buyers Go Happy</a></td><td>Designer</td><td>Work in home</td><td>4000</td><td>09-06-2018</td><td><button class='btn-primary apply'>Apply</button></td></tr>");

$(".table").append("<tr><td><a href='#'>Google</a></td><td>Testing</td><td>Fulltime</td><td>10000</td><td>22-05-2018</td><td><button class='btn-primary apply'>Apply</button></td></tr>");

$(".table").append("<tr><td><a href='#'>TCS</a></td><td>Marketing</td><td>Parttime</td><td>5000</td><td>12-06-2017</td><td><button class='btn-primary'>Apply</button></td></tr>");

$(".table").append("<tr><td><a href='#'>Microsoft</a></td><td>Developer</td><td>Fulltime</td><td>8000</td><td>02-10-2016</td><td><button class='btn-primary'>Apply</button></td></tr>");

$("#search").keyup(function(){
input = document.getElementById("search");
filter = input.value.toUpperCase();

 
 for (i = 1; i < tr.length; i++)
    {
     td = tr[i].getElementsByTagName("td")[0];
      if(td)
         {
           if(td.textContent.toUpperCase().startsWith(filter))
           {
             tr[i].style.display = "";
           }
           else
           {
             tr[i].style.display = "none";
           }
         }       
   }  
});

$("#jobs").text(tr.length - 1);

$(".apply").click(function(){  
 alert("Successfully Applied.");
})