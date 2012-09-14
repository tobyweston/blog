---
layout: post
title: "Diff Excel with Java and Hamcrest"
date: 2012-09-14 13:21
comments: true
categories: java recipes
sidebar: false
published: true
keywords: "excel, diff, compare excel, testing excel, testing, junit, hamcrest, java"
description: "Diff Excel using Java and Hamcrest. Build and compare Excel files using Java and Hamcrest."
---

Comparing Excel spreadsheets programmatically can be tricky. Projects like [Apache POI](http://poi.apache.org/) and [JExcel](http://jexcelapi.sourceforge.net/) let you build and interrogate sheets but don't offer a built in compare function. Fortunately, [simple-excel](http://github.com/tobyweston/simple-excel) offers a simplified API for building sheets in Java and a bunch of [Hamcrest](http://hamcrest.org/) matchers to find differences.

<!-- more -->

## Building Spreadsheets

[Simple-excel](http://github.com/tobyweston/simple-excel) takes a sheet as a template and allows you to apply changes programmatically to it. For example, you can start with a blank invoice sheet and insert items and totals from your Java code. It wraps Apache POI to make things easier to work with.

However you create your sheet, it'd be nice to be able to unit test it. [Simple-excel](http://github.com/tobyweston/simple-excel) offers `Matcher`s to do just that. You can write unit style tests, making assertions against individual cells or rows or you can write coarser grained tests that compare every cell of one sheet against every cell of another.

## Matchers

The matchers you're most likely to use can be found in the `bad.robot.excel.matchers.Matchers` class. They include `WorkbookMatcher` and `CellMatcher` but there are a bunch of finer grained matchers in the `bad.robot.excel.matchers` package.

## Comparing Sheets

Using the `WorkbookMatcher`, you can compare an entire workbook to another. The comparison is made against POI `Workbook` objects, so load these using the POI.

{% codeblock lang:java %}
Workbook actual = new HSSFWorkbook(...);
Workbook expected = new HSSFWorkbook(...);
assertThat(actual, sameWorkbook(expected));
{% endcodeblock %}


If you use the `MatcherAssert.assertThat` from Hamcrest rather than the vanilla JUnit version (`org.junit.Assert.assertThat`), you'll see useful information on a failure.

    java.lang.AssertionError:
    Expected: entire workbook to be equal
         but: cell at "C14" contained <"bananas"> expected <nothing>,
              cell at "C15" contained <"£1,850,000"> expected <"£1,850,000.00">,
              cell at "D16" contained <nothing> expected <"Tue Sep 04 06:30:00">


Other failures might include differing number of sheets, differently named sheets, different number of rows or columns. They're all aggregated in the failure message so you don't need to fix one and run the test again. It'll try and report all errors up front.


## Finer Grained Comparisons

Lets say we have a class, `InvoiceItem` representing a sale item. We'd like to append this line item to an invoice. It might look something like this.

{% codeblock lang:java %}
InputStream template = this.getClass().getResourceAsStream("invoiceTemplate.xls");
Workbook invoice = new HSSFWorkbook(template);
InvoiceItem item = new InvoiceItem();
item.appendTo(invoice);
{% endcodeblock %}

The `appendTo` method uses [simple-excel](http://github.com/tobyweston/simple-excel) to append the row to the invoice (ignore the details for now) but we'd like to verify that the sheet has been modified in the right way. Using the `CellMatcher`, you can do something like this.

{% codeblock lang:java %}
assertThat(getCellForCoordinate(coordinate(E, 1), invoice), is(equalTo(stringCell("Mac Book Pro"))));
assertThat(getCellForCoordinate(coordinate(E, 2), invoice), is(equalTo(numberCell(999.99D))));
assertThat(getCellForCoordinate(coordinate(E, 3), invoice), is(equalTo(blankCell()));
{% endcodeblock %}

Where the `getCellForCoordinate` returns a POI `Cell` object and `equalTo` is statically imported from `bad.robot.excel.matchers.Matchers` (not regular Hamcrest `equalTo`);

When it fails, you'll get something friendly like this;

	java.lang.AssertionError:
	Expected: is <999.99D>
		 but: cell at "E2" contained <1999.99D> expected <999.99D>

It matches on type and content of the cell. So the string cell `"999.99"` is different than the numeric cell `999.99`.



The project is open source. As always, I'd love to hear how you get on using it. Check out the leave me a comment if you like it. Issues are tracked on the [project site](http://github.com/tobyweston/simple-excel/issues).

