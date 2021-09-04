defmodule Main do
  def main do
    s1 = IO.read(:line) |> String.trim()
    s2 = IO.read(:line) |> String.trim()
    s3 = IO.read(:line) |> String.trim()
    solve([s1, s2, s3]) |> IO.puts()
  end

  def solve(li) do
    [ "ABC", "ARC", "AGC", "AHC" ] -- li
  end

end
