unit grid;

interface 
    const rows = 6; 
          cols = 5;


    type matrix = array[1..rows , 1..cols] of smallint;

    function getGrid() : matrix;
    procedure printGrid(grid : matrix);

implementation 

function getGrid() : matrix;

    var i , j: integer;
        result : matrix;

    begin
        for i := 1 to rows do 
            for j := 1 to cols do 
                result[i , j] := random(2);
        
        getGrid := result;
    end;
    


procedure printGrid(grid : matrix);

    var i , j : integer;

    begin   
        for i := 1 to rows do
            begin
                for j := 1 to 30 do 
                    write(' ');
                for j := 1 to cols do 
                    write(grid[i , j] , ' ');
                writeln;  
            end;
    end;

begin 
end.

