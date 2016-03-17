#!/usr/bin/env python

import sys
#import cProfile

class WordPath(object):

    def __init__(self, args):
        self.args = args
        self.dict_words, self.start, self.end = self.__unpack_args(args)

    def findPath(self):
        self.path = self.__buildGraph(self.start, self.end, self.dict_words)
        if self.path is None:
          print "%s: no path from '%s' to '%s'" % (sys.argv[0], self.start, self.end)
          exit(1)
        else:
            print self.__str()
        return 0

    def __unpack_args(self, args):
      dict_path = "/usr/share/dict/words"
      if len(args) < 2 or len(args) > 3:
        print "Usage: " + sys.argv[0] + " /usr/share/dict/words start_word end_word"
        exit(1)
      start, end = args[0:2]
      if len(args) == 3:
        dict_path = args[2]
      return (start, end, dict_path)

    def __steps(self, start, end, begat):
      path = [end]
      while path[-1] != start:
        path.append(begat[path[-1]])
      path.reverse()
      return path

    def __read_words(self, path):
      ws = []
      try:
        f = open(path, "r")
      except IOError, (errno, error):
        print "%s: open %s: %s\n" % (sys.argv[0], path, error)
        exit(1)
      for w in f:
        ws.append(w[:-1].lower())
      return ws

    def __buildGraph(self, start, end, dict):
      if len(start) != len(end):
        return None
      ws = self.__read_words(dict)
      cdates = set([w for w in ws if len(w) == len(start)])
      start = start.lower()
      end  = end.lower()
      b = {}
      l = [start]
      while len(l) > 0:
        f = []
        for w in l:
          neighbor = [n for n in cdates if self.__hop(n, w)]
          for n in neighbor:
            b[n] = w
            cdates.remove(n)
          if end in neighbor:
            return self.__steps(start, end, b)
          else:
            f.extend(neighbor)
        l = f
      else:
        return None

    def __hop(self, x, y):
      h = 0
      for xx, yy in zip(x, y):
        if xx != yy:
          h += 1
      return h == 1


    def __str(self):
        if self.path[0]:
            return ' -> '.join(self.path)
        else:
            return ''



def main(args):

  word_path = WordPath(args)
  word_path.findPath()

  return 0

if __name__ == "__main__":
    #cProfile.run('main(sys.argv[1:])')
    main(sys.argv[1:])
