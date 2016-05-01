import Data.List

nFlips :: [Char] -> Int
nFlips xs = nGroups xs - (if lastIsPlus xs then 1 else 0)
    where nGroups = length . group
          lastIsPlus = (=='+') . last

prependCaseNumber :: [String] -> [String]
prependCaseNumber = zipWith prep [1..]
    where prep n s = "Case #" ++ show n ++ ": " ++ s

main = do
    input <- getContents
    let inputs = tail $ lines input
        result = prependCaseNumber $ map (show . nFlips) inputs
    mapM putStrLn result
