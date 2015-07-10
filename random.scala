import io.Source.stdin
import scala.math
import scala.math.BigDecimal

object Solution {

	def main(args: Array[String]) {
		val lines = stdin.getLines
		val num = lines.next.toInt

		val l = lines.next.split(" ").map(_.toInt)
		
		val ret = ratios(l)
		println(ret._1)
		println(ret._2)
		println(ret._3)
	}

	def ratios(l: Array[Int]): Tuple3[String,String,String] = {
		val count = l.length.toDouble
		val n1 = l.filter(_ > 0).length / count
		val n2 = l.filter(_ == 0).length / count
		val n3 = l.filter(_ < 0).length / count

		(f"$n1%.3g%n", f"$n2%.3g%n", f"$n3%.3g%n")
	}

	def bigSum(numbers: List[Long]): Long = {
		numbers.foldLeft(0L) { _ + _ }
	}

	def diagonalDiff(matrix: Array[Array[Int]]): Int = {
		// var arr: Array[Array[Int]] = new Array(num)

		// var i = 0
		// lines.foreach { x =>
		// 	val y = x.split(" ").toArray.map { _.toInt }
		// 	arr(i) = y
		// 	i += 1
		// }

		val rows = matrix.length

		var sum1 = 0
		var sum2 = 0
		var diagonalPosition = 0
		matrix.foreach { x =>
			sum1 += x(diagonalPosition)
			sum2 += x(rows - diagonalPosition - 1)
			diagonalPosition += 1
		}

		math.abs(sum1 - sum2)
	}

}