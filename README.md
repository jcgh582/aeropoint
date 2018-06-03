## install

- Make sure you have docker installed and it is running
- ./install

## run example

- ./grab_data nybp 2018-06-01T23:11:22Z 2018-06-02T01:33:44Z

## run tests

- ./run_tests -v

## results

- output/result will be in example.obs

## intermediate data

- zipped and unzipped files downloaded from ftp server will be in rawData directory

## other relevant info

- if an exception is thrown, you will get a stack trace
- I have added the teqc binary to my source repo. It's not ideal, but it makes installing the application easier

## Assumptions

- I assume the start and end datetime will always be UTC iso8601 e.g.
    - good: 2018-06-01T23:11:22Z
    - bad: 2018-06-01T23:11:22

