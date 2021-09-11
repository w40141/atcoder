efmodule Main do
  def main do
    [x, y] = IO.read(:line) |> String.trim() |> String.split(" ")
    solve(x, y) |> IO.puts()
  end

  @doc ~S"""
  https://atcoder.jp/contests/abc217/tasks/abc217_a

  ## Examples

      iex> A.solve(abc, atcoder)
      "Yes"

      iex> A.solve(arc, agc)
      "No"

      iex> A.solve(a, aa)
      "Yes"

  """
  def solve(x, y) do
    answer(x > y)
  end

  def answer(true), do: "No"
  def answer(false), do: "Yes"
end
