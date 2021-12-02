except Exception:
except BaseException:
except ArithmeticError:
except BufferError:
except LookupError:
except AssertionError:
except AttributeError:
except EOFError:
except FloatingPointError:
except GeneratorExit:
except ImportError:
except ModuleNotFoundError:
except IndexError:
except KeyError:
except KeyboardInterrupt:
except MemoryError:
except NameError:
except NotImplementedError:
except OSError([arg]):
except OSError(errno, strerror[, filename[, winerror[, filename2]]]):
except OverflowError:
except RecursionError:
except ReferenceError:
except RuntimeError:
except StopIteration:
except StopAsyncIteration:
except SyntaxError:
except IndentationError:
except TabError:
except SystemError:
except SystemExit:
except TypeError:
except UnboundLocalError:
except UnicodeError:
except UnicodeEncodeError:
except UnicodeDecodeError:
except UnicodeTranslateError:
except ValueError:
except ZeroDivisionError:
except EnvironmentError:
except IOError:
except WindowsError:
except BlockingIOError:
except ChildProcessError:
except ConnectionError:
except BrokenPipeError:
except ConnectionAbortedError:
except ConnectionRefusedError:
except ConnectionResetError:
except FileExistsError:
except FileNotFoundError:
except InterruptedError:
except IsADirectoryError:
except NotADirectoryError:
except PermissionError:
except ProcessLookupError:
except TimeoutError:
except Warning:
except UserWarning:
except DeprecationWarning:
except PendingDeprecationWarning:
except SyntaxWarning:
except RuntimeWarning:
except FutureWarning:
except ImportWarning:
except UnicodeWarning:
except BytesWarning:
except ResourceWarning:

try:
     pass
except Exception:
     pass
else:
     pass
finally:
     pass

try:
      f=open('Car_game.py')
except FileNotFoundError as e:
     print(e)
except Exception as e:
     print(e)
else:
     print(f.read())
     f.close()
finally:
     print('Executing Finally...')
