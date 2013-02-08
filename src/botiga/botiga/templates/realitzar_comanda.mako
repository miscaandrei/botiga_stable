<html>
   <body>
      <h1>${projecte}</h1>
      <ul>
          <form>
              <table border='1' >
                <tr>
                    <td>
                        % for prod in diccionari:
                            ${diccionari[prod]['Name']}: </td><td> <input type="text" name=${prod} value='0' ><br>
                            </td>
                    </tr>
                        % endfor
                    
                </table>
            </form>
      </ul><br>
   </body>
</html>
