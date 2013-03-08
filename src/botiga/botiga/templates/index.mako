<html>
<head>
   <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
   <a href='/index'><title>${projecte}</title></a>
</head>
   <body>
      <h1>${projecte}</h1>
      <ul>
      % for elements in menu:
         <a href=${menu[elements]}><li>${elements}</li></a>
      % endfor
      </ul>
      <p>Make your choice!</p>
   </body>
</html>
