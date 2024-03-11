unit land;

interface 

    uses grid;

    function countLands(grid : matrix) : integer;


implementation

function checkIndex(i , j : integer) : boolean;

    begin
        checkIndex := (i > 0) and (i <= rows) and (j > 0) and (j <= cols); 
    end;

function checkBefore(grid : matrix ; i , j : integer) : boolean;

    begin
        if (checkIndex(i, j - 1)) then 
            checkBefore := (grid[i , j - 1] = 1)
        else 
            checkBefore := FALSE;
    end;

function checkTop(grid : matrix ; i , j : integer) : boolean;

    begin
        if (checkIndex(i - 1, j)) then 
            checkTop := (grid[i - 1 , j] = 1)
        else 
            checkTop := FALSE;
    end;

function checkTopRight(grid : matrix ; i , j : integer) : boolean;

    begin
        if (checkIndex(i - 1 , j + 1)) then 
            checkTopRight := (grid[i - 1 , j + 1] = 1)
        else 
            checkTopRight := FALSE;
    end;

function checkAfter(grid : matrix ; i , j : integer) : boolean;

    begin
        if (checkIndex(i , j + 1)) then 
            checkAfter := (grid[i , j + 1] = 1)
        else 
            checkAfter := FALSE;
    end;

// function checkBefore(grid : matrix ; i , j : integer) : boolean;

//     begin
//         if (checkIndex(i, j - 1)) then 
//             checkBefore := (grid[i , j - 1] = 1)
//         else 
//             checkBefore := FALSE;
//     end;

// function checkBefore(grid : matrix ; i , j : integer) : boolean;

//     begin
//         if (checkIndex(i, j - 1)) then 
//             checkBefore := (grid[i , j - 1] = 1)
//         else 
//             checkBefore := FALSE;
//     end;

function check(grid : matrix ; i , j : integer) : boolean;

    begin
        check := (grid[i , j] = 1);
        check := check and (not checkBefore(grid , i , j));
        check := check and (not checkTop(grid , i , j));
        check := check and (not (checkAfter(grid , i, j) and (checkTopRight(grid , i , j)))); 
    end;


function countLands(grid : matrix) : integer;

    var count : integer;
        i , j : integer;
    
    begin
        count := 0;

        for i := 1 to rows do 
            for j := 1 to cols do 
                if (check(grid , i , j)) then 
                    begin 
                        writeln('found at : ' , i , ' ' ,j);
                        count := count + 1;
                    end;
                    
        countLands := count;
    end;


begin 
end.