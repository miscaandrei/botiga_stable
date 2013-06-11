<html>
   <body>
      <a href='/index'><h1>${projecte}</h1></a>
      <ul>
        <table border='1' >
            <tr>
                <td>ID Producte</td>
                <td>Nom</td>
                <td>Preu</td>
                <td>Unitats Disponibles</td>
            </tr>
            <tr>
                % for prod in diccionari:
                    <td>${prod}</td>
                    <td>${diccionari[prod]['Name']}</td>
                    <td>${diccionari[prod]['Price']}</td>
                    <td>${diccionari[prod]['Stock']}</td>
            </tr>
                % endfor
        </table>
      </ul><br>
      <span tal:condition="logged_in">
   <a href="${request.application_url}/logout">Logout</a>
</span>
   </body>
</html>
