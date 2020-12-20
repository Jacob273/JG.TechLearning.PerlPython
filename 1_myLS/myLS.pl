#!/usr/bin/perl
use Getopt::Std;

sub printStarsFunction {
    my @b = (1..40);
    for(@b){
        print "*";
    }

            print "\n";
  }

sub openDirectoryFunction{
    my $path = shift;
    opendir(my $handler, $path) || die "Can't open directory $directoryFilesToBePrintedOut";
    return $handler;
}


printStarsFunction();
print "STARTING ls SIMULATOR. (print files inside given folder)\n";
printStarsFunction();

# Getting value from args or using dot

$directoryFilesToBePrintedOut;
if(@ARGV)
{
    $directoryFilesToBePrintedOut = @ARGV[0];
}
else
{
    $directoryFilesToBePrintedOut = '.';
}

#Opening directory
my $handler = openDirectoryFunction($directoryFilesToBePrintedOut);
@filesList = sort(readdir($handler));
closedir $handler;

foreach $item ( @filesList ) 
{
    # The stat() function gets status information about a specified file 
    my $size = (stat("$directoryFilesToBePrintedOut/$item"))[7];
    my $mode = (stat("$directoryFilesToBePrintedOut/$item"))[2];
    $result = sprintf("Item: %30s   ||  size [ %08d ] bytes || permissions [ %04o ]     ", $item,  $size, $mode & 07777);
    print("$result \n");
}

