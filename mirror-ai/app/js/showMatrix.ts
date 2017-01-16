
function toAdjacency(M: number[][])
{   let output = [];
    for (let i = M.length - 1; i >= 0; i--)
    {   for (let j = M[i].length - 1; j >= 0; j--)
        {   if (M[i][j] > 0)
            {   let grid = {
                        id: `${i}-${j}`,
                        x: i,
                        y: j,
                        weight: M[i][j]
                    };
                output.push(grid);
            }
            else {}
        }
    }
    return output;
}

