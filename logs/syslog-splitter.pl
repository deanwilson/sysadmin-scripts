#!/usr/bin/perl -w
use strict;
use warnings;

# take arguments and do a summary of the lines in each - or do a wc?

my $outputdir = 'out';
my %facilities;

unless ( -d $outputdir) {
  mkdir( $outputdir )
    || die "Failed to create [$outputdir]: $!\n";
}

while( defined ( my $line = <> ) ) {
  my $facility = (split( /\s+/, $line ))[4];
  $facility =~ s/\[\d+\]://;
  $facility =~ s!/!_!g;

  unless ( defined $facilities{$facility} ) {
    $facilities{$facility} = open_split_log( $facility );
  }

  print { $facilities{$facility} } $line;
}

############################################################

sub open_split_log {
  my $facility = shift;

  open( my $split_log_fh, '>', "$outputdir/$facility" )
    || die "Failed to open [$outputdir/$facility]: $!\n";

  return $split_log_fh;
}
