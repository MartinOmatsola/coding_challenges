import io.Source.stdin
import scala.math
import scala.math.BigDecimal

object Solution {

	def main(args: Array[String]) {
		// val lines = stdin.getLines
		// val num = lines.next.toInt

		// val l = lines.next.split(" ").map(_.toInt)
		
		// val ret = ratios(l)
		// println(ret._1)
		// println(ret._2)
		// println(ret._3)
		// drawStairs(num)

		println(largest3digitPalindromeProduct())
	}

	def isPalindrome(s: String): Boolean = {
		var stop: Int = s.length / 2
		var start = if (s.length % 2 == 0) stop else (stop + 1)
		
		val s1 = s.substring(0, stop)
		val s2 = s.substring(start).reverse

		s1.equals(s2)
	}

	def largest3digitPalindromeProduct(): Int = {
		val l = scala.collection.mutable.ArrayBuffer.empty[Int]
		for (i <- 100 to 999) {
			for (j <- 100 to 999) {
				val k = i * j
				if (isPalindrome(k.toString)) {
					l += k
				}
			}
		}

		l.max
	}

	def largestPrime(num: Double): Double = {
		val l = scala.collection.mutable.ArrayBuffer.empty[Double]
		var d = 2
		var n = num
		var flag = true
		while (n > 1 && flag) {
			while (n % d == 0) {
				l += d
				n = n / d
			}
			d += 1
			if (d * d > n) {
				if (n > 1) { 
					l += n
				}
				flag = false
			}
		}

		l.max
	}

	def fib(): Long = {
		var n1: Long = 1
		var n2: Long = 2
		var sum: Long = 2
		while (n1 + n2 < 4000000) {
			val fib = n1 + n2
			if (fib % 2 == 0)
				sum += fib
			n1 = n2
			n2 = fib
		}

		sum
	}

	def sumMultipleOf3or5(upperBound: Int): Int = {
		(1 until upperBound).toList.filter { x =>
			(x % 3 == 0) || (x % 5 == 0) 
		}.sum
	}

	def drawStairs(n: Int) {
		for (i <- 1 to n) {
			for (k <- 1 to (n-i)) print(" ")
			for (j <- (n-i+1) to n) print("#")
			println("")
		}
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