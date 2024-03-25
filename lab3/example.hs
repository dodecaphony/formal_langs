data Maybe a = Nothing | Just a

sum :: Int -> Int -> Int
sum x y = x + y

main :: IO ()
main = print (sum 5 3)