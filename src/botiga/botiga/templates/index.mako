<html>
<head>
   <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
   <title>${projecte}</title>
</head>
   <body>
      <h1>Welcome</h1>
      <ul>
      % for elements in menu:
         <a href=${menu[elements]}><li>${elements}</li></a>
      % endfor
      </ul>
      <p>Make your choice!</p>
   </body>
</html>
