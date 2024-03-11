uses grid , land;

procedure main();

    var grid : matrix;
        numberLands : integer;

    begin
        randomize;

        grid := getGrid();
        printGrid(grid); 

        numberLands := countLands(grid);

        writeln('the number of lands in the grid is : ' , numberLands);
    end;

begin
    main();
end.