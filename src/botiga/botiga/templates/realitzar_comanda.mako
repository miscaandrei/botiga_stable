<html>
   <body>
      <a href='/index'><h1>${projecte}</h1></a>
      <ul>
          <form action="${request.route_url('realitzar_comanda')}" method="post">
          <table border='1' >
            <tr>
                <td>ID Producte</td>
                <td>Nom</td>
                <td>Preu</td>
                <td>Unitats Disponibles</td>
                <td> Unitats Desitjades</td>
            </tr>
            <tr>
                % for prod in diccionari:
                    <td>${prod}</td>
                    <td>${diccionari[prod]['Name']}</td>
                    <td>${diccionari[prod]['Price']}</td>
                    <td>${diccionari[prod]['Stock']}</td>
                    <td><input type="text" maxlength="100" name=${prod}></br></td>
            </tr>
                % endfor
        </table>
        <input type="submit" name="add" value="Afegir" class="button">
          </form>
      </ul><br>
   </body>
</html>
