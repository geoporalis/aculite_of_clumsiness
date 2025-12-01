const std = @import("std");
const input = @embedFile("input");

pub fn main() !void {
    var it = std.mem.splitScalar(u8, input, '\n');
    var dail: i16 = 50;
    var p1: u16 = 0;
    var p2: u16 = 0;
    while (it.next()) |ln| {
        var dist = try std.fmt.parseInt(u16, ln[1 .. ln.len - 1], 10);
        while (dist > 0) : (dist -= 1) {
            dail += if (ln[0] == 'R') 1 else -1;
            if (ln[0] == 'L' and dail < 0) dail = 99;
            if (ln[0] == 'R' and dail < 99) dail = 0;
            if (dail == 0) p2 += 1;
        } else if (dail == 0) p1 += 1;
    } else std.debug.print("first {}\nsecond {}\n", .{ p1, p2 });
}
