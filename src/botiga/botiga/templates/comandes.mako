<html>
   <body>
      <a href='/index'><h1>${projecte}</h1></a>
      <ul>
        <table border='1' >
            <tr>
                <td>ID Commanda</td>
                <td>Nom</td>
                <td>Quantitat</td>
            </tr>
            <tr>
                % for prod in diccionari:
                    <td>${diccionari[prod]['ID_Commanda']}</td>
                    <td>${diccionari[prod]['Nom']}</td>   
                    <td>${diccionari[prod]['Quantitat']}</td>

            </tr>
                % endfor
        </table>
      </ul><br>
      <span tal:condition="logged_in"><a href="${request.application_url}/logout">Desconectat</a></span>
   </body>
</html>
