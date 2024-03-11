unit game;

interface 

    uses CRT;

    const ROWS = 15; COLS = 25;
        size = 25;

    type matrix = array[1..ROWS , 1..COLS] of char;
        couple = record 
            x ,y : integer;
            // x for cols , y for rows!
        end;

    function initGrid() : matrix;
    procedure printGrid(grid : matrix);
    procedure putCandy(var grid : matrix ; candyPosition : couple);
    procedure run(numberCandies : integer);
    procedure setRandomCandy(var grid: matrix ; var candyPosition : couple);

implementation

function getRandomCouple() : couple;

    var result : couple;

    begin
        result.x := random(COLS) + 1;
        result.y := random(ROWS) + 1;

        getRandomCouple := result; 
    end;

function initGrid() : matrix;

    var result : matrix;    
        i , j: integer;
    
    begin
        for i := 1 to ROWS do 
            for j := 1 to COLS do 
                result[i , j] := ' ';
        
        initGrid := result;
    end;

procedure printTab(size : integer);

    var i : integer;

    begin
        for i := 1 to size do 
            write(' '); 
    end;

procedure printGrid(grid : matrix);

    var i , j : integer;

    begin
        printTab(size + 1);

        for j := 1 to COLS do 
            write('_');
        
        writeln;

        for i := 1 to ROWS do 
            begin 
                printTab(size);

                write('|');

                for j := 1 to COLS do 
                    write(grid[i , j]);

                writeln('|');
            end;
        
        printTab(size);

        write('|');

        for j := 1 to COLS do 
            write('_');  

        writeln('|');       
    end;

function getAnt() : char;

    begin
        getAnt := '#'; 
    end;

function getCandy() : char;

    begin
        getCandy := '*'; 
    end;

procedure initCell(var grid : matrix ; position : couple);

    begin
        grid[position.y , position.x] := ' '; 
    end;

procedure putAnt(var grid : matrix ; currentPosition : couple);

    begin
        grid[currentPosition.y , currentPosition.x] := getAnt(); 
    end;

procedure putCandy(var grid : matrix ; candyPosition : couple);

    begin
        grid[candyPosition.y , candyPosition.x] := getCandy();
    end;

procedure moveAntX(var currentPosition , vector : couple);

    begin
        if (currentPosition.x + vector.x > COLS) then 
            vector.x := -1
        else 
            if (currentPosition.x + vector.x < 1) then 
                vector.x := 1;

        currentPosition.x := currentPosition.x + vector.x;
    end;

procedure moveAntY(var currentPosition , vector : couple);

    begin
        if (currentPosition.y + vector.y > ROWS) then 
            vector.y := -1
        else 
            if (currentPosition.y + vector.y < 1) then 
                vector.y := 1; 
            
        currentPosition.y := currentPosition.y + vector.y
    end;

function getVectorX(currentPosition , candyPosition : couple) : couple;

    var vector : couple;

    begin
        vector.x := 0;

        if (currentPosition.x > candyPosition.x) then 
            vector.x := -1 
        else 
            if (currentPosition.x < candyPosition.x) then 
                vector.x := 1;
            
        vector.y := 0;  
        getVectorX := vector;
    end;

function getVectorY(currentPosition , candyPosition : couple) : couple;

    var vector : couple;

    begin
        vector.y := 0;

        if (currentPosition.y > candyPosition.y) then 
            vector.y := -1 
        else 
            if (currentPosition.y < candyPosition.y) then 
                vector.y := 1;

        vector.x := 0;
        getVectorY := vector; 
    end;

procedure setAntX(var grid : matrix ; var currentPosition , candyPosition : couple);

    var vector: couple;

    begin
        initCell(grid , currentPosition);
        vector := getVectorX(currentPosition , candyPosition);
        moveAntX(currentPosition , vector);
        putAnt(grid , currentPosition); 
    end;

procedure setAntY(var grid : matrix ; var currentPosition , candyPosition : couple);

    var vector : couple;

    begin
        initCell(grid , currentPosition);
        vector := getVectorY(currentPosition , candyPosition);
        moveAntY(currentPosition , vector);
        putAnt(grid , currentPosition); 
    end;


procedure setRandomCandy(var grid: matrix ; var candyPosition : couple);

    begin
        initCell(grid , candyPosition);
        candyPosition := getRandomCouple();
        putCandy(grid , candyPosition);
    end;

function AntEatsCandy(currentPosition , candyPosition : couple): boolean;

    begin
        AntEatsCandy := (currentPosition.x = candyPosition.x) and (currentPosition.y = candyPosition.y); 
    end;

procedure tellPosition(position : couple);

    begin
        writeln('rows : ' , position.y);
        writeln('cols : ' , position.x); 
    end;

procedure run(numberCandies : integer);

    var currentPosition , candyPosition , vector: couple;
        candies : integer;
        grid : matrix;
        round : boolean;

    begin
        round := TRUE;

        grid := initGrid();

        currentPosition := getRandomCouple();
        candyPosition := getRandomCouple();
        candies := 0;
    
        putAnt(grid , currentPosition);
        putCandy(grid , candyPosition);


        while (candies <> numberCandies) do 
            begin
                clrscr;
                printGrid(grid);

                writeln;

                if (round) then
                    begin 
                        vector := getVectorX(currentPosition , candyPosition);
                        setAntX(grid , currentPosition , candyPosition);
                    end
                else 
                    begin 
                        vector := getVectorX(currentPosition , candyPosition);
                        setAntY(grid , currentPosition , candyPosition);
                    end;
                
                round := not round;

                if (AntEatsCandy(currentPosition , candyPosition)) then 
                    begin 
                        inc(candies);
                        setRandomCandy(grid , candyPosition);
                    end;

                writeln('number of candies collected : ' , candies);
            
                delay(50);
                
                
                
            end;
    end;




begin 
end.