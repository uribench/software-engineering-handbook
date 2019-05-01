# String Calculator Example

## TDD Development Steps

1.  Write a failing test
2.  Implement the production code necessary to make the test past.
3.  Refactor and remove _all_ duplication.

## Exercise

1. Given a single number in a string, return the number

  Write a failing test.
  ```java
  public class StringCalculatorTest {
    @Test
    public void singleOneInStringReturnOne() {
      StringCalculator calculator = new StringCalculator();
      assertEquals(1, calculator.add("1"), 0);
    }
  }
  ```

  Write _only_ enough code to make the test pass
  ```java
  public class StringCalculator {
    public int add(String numbers) {
      return 1;
    }
  }
  ```

  This isn't quite enough though to prove that a single number will _always_ return that number as an int therefore we need another test.

  Write another failing test.

  ``` java
  ...
  @Test
  public void singleTwoInStringReturnsTwo() {
    StringCalculator calculator = new StringCalculator();
    assertEquals(2, calculator.add("2"), 0);
  }
  ...
  ```

  Write the code that makes the test pass.

  ``` java
  ...
  public int add(String numbers) {
    return Integer.parseInt(numbers);
  }
  ...
  ```

  Now refactor and remove duplication. (Even in the test code)

  ```java
  public class StringCalculatorTest {
    private static final int DELTA = 0;
    private StringCalculator calculator;

    @Before
    public void setup() {
      this.calculator = new StringCalculator();
    }

    @Test
    public void singleOneInStringReturnOne() {
      assertEquals(1, this.calculator.add("1"), DELTA);
    }

    @Test
    public void singleTwoInStringReturnsTwo() {
      assertEquals(2, this.calculator.add("2"), DELTA);
    }
  }
  ```
2. Given 2 comma delimited numbers, return the sum

  Write the failing test.
  ```java
  ...
  @Test
  public void twoCommaDelimitedStringReturnSum() {
    assertEquals(3, this.calculator.add("1,2"), DELTA);
  }
  ...
  ```

  When the tests are run, an exception will be thrown instead of a failed assertion (`java.lang.NumberFormatException: For input string: "1,2"`).  This will need to be fixed _before_ we can implement the logic to satisfy the test.

  ```java
  ...
  public double add(final String numbers) {
    if (numbers.matches("[0-9]+")) {
      return Integer.parseInt(numbers);
    }

    return Integer.MIN_VALUE;
  }
  ...
  ```

  Now that the tests execute without errors, we can now implement what is necessary to satisfy the test.

  ```java
  ...
  public double add(final String numbers) {
    if (numbers.matches("[0-9]+")) {
      return Integer.parseInt(numbers);
    }

    if (numbers.contains(",")) {
      String[] numberParts = numbers.split(",");
      return Integer.parseInt(numberParts[0]) + Integer.parseInt(numberParts[1]);
    }

    return Integer.MIN_VALUE;
  }
  ...
  ```

  Execute the tests and watch everything turn green.
3. Given multiple comma delimited numbers, return the sum

  Write the failing test
  ```java
  ...
  @Test
  public void multipleCommaSeparatedNumbersReturnSum() {
    assertEquals(3, calculator.add("1,1,1"), DELTA);
  }
  ...
  ```

  After executing this test, you will notice that it is only adding up the first two numbers, because that's the way it was written, let's fix that.

  ```java
  ...
  public double add(final String numbers) {
    if (numbers.matches("[0-9]+")) {
      return Integer.parseInt(numbers);
    }

    if (numbers.contains(",")) {
      return Pattern.compile(",")
        .splitAsStream(numbers)
        .mapToInt(Integer::parseInt)
        .sum();
    }

    return Integer.MIN_VALUE;
  }
  ...
  ```

  Now for good measure, let's add an additional assertion to the test to assert that multiple numbers are supported completely.
  ```java
  ...
  @Test
  public void multipleCommaSeparatedNumbersReturnSum() {
    assertEquals(3, calculator.add("1,1,1"), DELTA);
    assertEquals(21, calculator.add("1,2,3,4,5,6"), DELTA);
  }
  ...
  ```
4. Allow new line delimited (\n) string instead of commas

  Now instead of only allowing commas as a delimiter, we now need to allow for new line characters (`\n`).  Write the failing test.
  ```java
  ...
  @Test
  public void multipleNewLineSeparatedNumbersReturnSum() {
    assertEquals(3, this.calculator.add("1/n1/n1"), DELTA);
  }
  ...
  ```

  Now let's make the necessary change to make the test pass.
  ```java
  ...
  public double add(final String numbers) {
    if (numbers.matches("[0-9]+")) {
      return Integer.parseInt(numbers);
    }

    if (numbers.contains(",")) {
      return Pattern.compile(",")
          .splitAsStream(numbers)
          .mapToInt(Integer::parseInt)
          .sum();
    }

    if (numbers.contains("/n")) {
      return Pattern.compile("/n")
          .splitAsStream(numbers)
          .mapToInt(Integer::parseInt)
          .sum();
    }

    return Integer.MIN_VALUE;
  }
  ...
  ```

  This has made the tests all pass but now we need to refactor to get rid of the duplication.
  ```java
  ...
  public double add(final String numbers) {
      if (numbers.matches("[0-9]+")) {
        return Integer.parseInt(numbers);
      }

      if (numbers.contains(",")) {
        return this.splitOnDelimiterAndSumNumbers(numbers, ",");
      }

      if (numbers.contains("/n")) {
        return this.splitOnDelimiterAndSumNumbers(numbers, "/n");
      }

      return Integer.MIN_VALUE;
    }

    private int splitOnDelimiterAndSumNumbers(String numbers, String delimiter) {
      return Pattern.compile(delimiter)
        .splitAsStream(numbers)
        .mapToInt(Integer::parseInt)
        .sum();
    }
    ...
  ```

  The tests provide the confidence necessary to refactor.  Execute the tests again to make sure nothing is broken and let's move on.

5. Support different delimiters (with any length), defined on the first line of the string prefixed with ``//``, example `"//;/n1;2"` would return 3

  Write the failing test.
  ```java
  ...
  @Test
  public void customDelimiterOnFirstLineReturnSum() {
    assertEquals(5, this.calculator.add("//;/n1;2;2"), DELTA);
  }
  ...
  ```

  Now there is another exception thrown, `java.lang.NumberFormatException: For input string: "//;"`, so we need to fix that first.  Not a very elegant solution, but it is a solution and that's all we are after right now.

  ```java
  ...
  if (numbers.contains("/n")) {
    if (!numbers.contains("//")) {
      return this.splitOnDelimiterAndSumNumbers(numbers, "/n");
    }
  }
  ...
  ```

  Now that the exception is taken care of, let's implement the logic to satisfy the test.

  ```java
  ...
  public double add(final String numbers) {
    if (numbers.matches("[0-9]+")) {
        return Integer.parseInt(numbers);
    }

    if (numbers.contains(",")) {
        return this.splitOnDelimiterAndSumNumbers(numbers, ",");
    }

    if (numbers.contains("//")) {
      String[] customDelimiterParts = numbers.split("/n");
      return this.splitOnDelimiterAndSumNumbers(
        customDelimiterParts[1],
        customDelimiterParts[0].substring(2));
    }

    if (numbers.contains("/n")) {
        return this.splitOnDelimiterAndSumNumbers(numbers, "/n");
    }

    return Integer.MIN_VALUE;
  }
  ...
  ```

  Since part of the requirement is a delimiter of _any length_ another assertion is necessary.

  ```java
  ...
  @Test
  public void customDelimiterOnFirstLineReturnSum() {
    assertEquals(5, this.calculator.add("//;/n1;2;2"), DELTA);
    assertEquals(15, this.calculator.add("//---/n1---2---2---10"), DELTA);
  }
  ...
  ```

  Now that we are happy we have met the requirement, let's move on.

6. If the string contains a negative number, throw an exception, the exception should contain 'negatives not allowed' and _all_ of the negative numbers in the message

  Write the failing test.  This is a slightly more complex test since we need to assert that the exception was not only thrown but also that the message contains all of the numbers.

  ```java
  ...
  @Test
    public void negativeNumbersThrowException() {
    try {
      this.calculator.add("1,2,-3,-5,7,-9");
      fail("Negative numbers did not throw exception");
    } catch (Exception e) {
      String message = e.getMessage();
      assertTrue(message.toLowerCase().contains("negatives not allowed"));
      assertTrue(message.contains("-3"));
      assertTrue(message.contains("-5"));
      assertTrue(message.contains("-9"));
    }
  }
  ...
  ```

  When this test runs, it currently fails because the exception is not thrown, so that's the first step.

  ```java
  ...
  private int splitOnDelimiterAndSumNumbers(String numbers, String delimiter) {
    boolean containsNegatives = Pattern.compile(delimiter)
      .splitAsStream(numbers)
      .mapToInt(Integer::parseInt)
      .filter(number -> number < 0)
      .findAny().isPresent();

    if (containsNegatives) {
      throw new IllegalArgumentException("Negatives");
    }

    return Pattern.compile(delimiter)
      .splitAsStream(numbers)
      .mapToInt(Integer::parseInt)
      .sum();
  }
  ...
  ```

  Now the test is failing because of the assertions on the message, let's add those to the message.

  ```java
  ...
  private int splitOnDelimiterAndSumNumbers(String numbers, String delimiter) {
    List<Integer> negatives = Pattern.compile(delimiter)
      .splitAsStream(numbers)
      .mapToInt(Integer::parseInt)
      .filter(number -> number < 0)
      .boxed()
      .collect(Collectors.toList());

    if (negatives.size() > 0) {
      throw new IllegalArgumentException("Negatives not allowed: " + negatives.toString());
    }

    return Pattern.compile(delimiter)
      .splitAsStream(numbers)
      .mapToInt(Integer::parseInt)
      .sum();
  }
  ...
  ```

  The `splitOnDelimiterAndSumNumbers()` is getting a bit too long, let's refactor a bit and extract the negative checking into another method.

  ```java
  ...
  private int splitOnDelimiterAndSumNumbers(String numbers, String delimiter) {
    this.checkForNegatives(numbers, delimiter);

    return Pattern.compile(delimiter)
      .splitAsStream(numbers)
      .mapToInt(Integer::parseInt)
      .sum();
  }

  private void checkForNegatives(String numbers, String delimiter) {
    List<Integer> negatives = Pattern.compile(delimiter)
      .splitAsStream(numbers)
      .mapToInt(Integer::parseInt)
      .filter(number -> number < 0)
      .boxed()
      .collect(Collectors.toList());

    if (negatives.size() > 0) {
      throw new IllegalArgumentException("Negatives not allowed: " + negatives.toString());
    }
  }
  ...
  ```

  That looks better and all tests are still green.

7. Numbers bigger than 1000 should be ignored.  ex. "1,1001,2" returns 3

  Write the final failing test.

  ```java
  ...
  @Test
  public void ignoreAllNumbersOver1000() {
    assertEquals(1003, this.calculator.add("//;/n1;2;1000;1001"), DELTA);
  }
  ...
  ```

  It turns out that this is a very simple addition.

  ```java
  ...
  private int splitOnDelimiterAndSumNumbers(String numbers, String delimiter) {
    this.checkForNegatives(numbers, delimiter);

    return Pattern.compile(delimiter)
      .splitAsStream(numbers)
      .mapToInt(Integer::parseInt)
      .filter(number -> number <= 1000)
      .sum();
  }
  ...
  ```

This is just one way to implement this class, I'm sure that you can come up with additional refactoring that can be done.  The best part of this code is that you can refactor anything you would like and the confidence is there that nothing has been broken by simply executing all of the tests and verifying that they all are green.

## Finished StringCalculatorTest Class

```java
package com.philips;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class StringCalculatorTest {
  private static final double DELTA = 0;
  private StringCalculator calculator;

  @Before
  public void setup() {
    this.calculator = new StringCalculator();
  }

  @Test
  public void stringOneReturnOne() {
    assertEquals(1, calculator.add("1"), DELTA);
  }

  @Test
  public void stringTwoReturnTwo() {
    assertEquals(2, calculator.add("2"), DELTA);
  }

  @Test
  public void twoCommaSeparatedNumbersReturnSum() {
    assertEquals(3, calculator.add("1,2"), DELTA);
  }

  @Test
  public void multipleCommaSeparatedNumbersReturnSum() {
    assertEquals(3, calculator.add("1,1,1"), DELTA);
    assertEquals(21, calculator.add("1,2,3,4,5,6"), DELTA);
  }

  @Test
  public void multipleNewLineSeparatedNumbersReturnSum() {
      assertEquals(3, this.calculator.add("1/n1/n1"), DELTA);
  }

  @Test
  public void customDelimiterOnFirstLineReturnSum() {
    assertEquals(5, this.calculator.add("//;/n1;2;2"), DELTA);
    assertEquals(15, this.calculator.add("//---/n1---2---2---10"), DELTA);
  }

  @Test
  public void negativeNumbersThrowException() {
    try {
      this.calculator.add("1,2,-3,-5,7,-9");
      fail("Negative numbers did not throw exception");
    } catch (Exception e) {
      String message = e.getMessage();
      assertTrue(message.toLowerCase().contains("negatives not allowed"));
      assertTrue(message.contains("-3"));
      assertTrue(message.contains("-5"));
      assertTrue(message.contains("-9"));
    }
  }

  @Test
  public void ignoreAllNumbersOver1000() {
    assertEquals(1003, this.calculator.add("//;/n1;2;1000;1001"), DELTA);
  }
}

```

## Finished StringCalculator Class

```java
package com.philips;

import java.util.List;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class StringCalculator {

  public double add(final String numbers) {
    if (numbers.matches("[0-9]+")) {
      return Integer.parseInt(numbers);
    }

    if (numbers.contains(",")) {
      return this.splitOnDelimiterAndSumNumbers(numbers, ",");
    }

    if (numbers.contains("//")) {
      String[] customDelimiterParts = numbers.split("/n");
      return this.splitOnDelimiterAndSumNumbers(
          customDelimiterParts[1],
          customDelimiterParts[0].substring(2));
    }

    if (numbers.contains("/n")) {
      return this.splitOnDelimiterAndSumNumbers(numbers, "/n");
    }

    return Integer.MIN_VALUE;
  }

  private int splitOnDelimiterAndSumNumbers(String numbers, String delimiter) {
    this.checkForNegatives(numbers, delimiter);

    return Pattern.compile(delimiter)
      .splitAsStream(numbers)
      .mapToInt(Integer::parseInt)
      .filter(number -> number <= 1000)
      .sum();
  }

  private void checkForNegatives(String numbers, String delimiter) {
    List<Integer> negatives = Pattern.compile(delimiter)
      .splitAsStream(numbers)
      .mapToInt(Integer::parseInt)
      .filter(number -> number < 0)
      .boxed()
      .collect(Collectors.toList());

    if (negatives.size() > 0) {
      throw new IllegalArgumentException("Negatives not allowed: " + negatives.toString());
    }
  }
}
```
