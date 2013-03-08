<html>
   <body>
      <h1>${projecte}</h1>
      <ul>
        <table border='1' >
            <tr>
                <td>ID Commanda</td>
                <td>Nom</td>
                <td>Quantitat</td>
            </tr>
            <tr>
                % for prod in diccionari:
                    <td>${prod}</td>
                    <td>${diccionari[prod]['Nom']}</td>   
                    <td>${diccionari[prod]['Quantitat']}</td>

            </tr>
                % endfor
        </table>
      </ul><br>
   </body>
</html>
